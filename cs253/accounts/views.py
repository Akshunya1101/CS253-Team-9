from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
import math
from django.contrib import messages
from django.db.models.signals import post_delete
from django.contrib.messages.views import SuccessMessageMixin
import json
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import Room, Message
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from .models import Sell, Seller, Customer, Order
from .forms import CreateUserForm, Sell_form
from math import ceil

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def home(request):
    products = Sell.objects.filter(seller=request.user)
    print(products)
    n = len(products)
    print(n)
    nSlides= n
    parameters={'no_of_slides':nSlides, 'range':range(1,nSlides), 'products': products}
    return render(request, 'accounts/dashboard.html', parameters)



def searchMatch(query, item):
	if(query.lower() in item.name.lower() or query.lower() in item.description.lower()):
		return True
	return False

@login_required(login_url='accounts:login')
def search(request):
	query = request.GET['search']
	products_temp = Sell.objects.all()
	products = [item for item in products_temp if searchMatch(query, item)]
	# products = Sell.objects.filter(title__icontains=query)
	return render(request, 'accounts/search.html', {'products': products})

@login_required(login_url='accounts:login')
def buy(request):
    context = {}
    return render(request, 'accounts/buy.html', context)


@login_required(login_url='accounts:login')
def rent(request):
    context = {}
    return render(request, 'accounts/rent.html', context)

@login_required(login_url='accounts:login')
def Sell_Create(request):
    form = Sell_form(request.POST, request.FILES)
    u_list = User.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        photo = request.FILES['photo']
        price = request.POST['price']
        seller = request.user
        if name=='' or description=='' or price=='' or seller=='':
            messages.success(request,'Kindly fill all the fields.')
            return render(request,'accounts/dashboard.html')
        Sell.objects.create(name=name, description=description, photo=photo, price=price, seller = seller)
        return redirect('accounts:home')
    return render(request, 'accounts/sell_form.html', {'form': form, 'u_list': u_list})


class Sell_List(ListView):
    model = Sell
    context_object_name = 'item_list'


class Sell_Details(DetailView):
    model = Sell


@login_required(login_url='accounts:login')
def enterRoom(request):
    return render(request, 'accounts/enterRoom.html')


@login_required(login_url='accounts:login')
def room(request, room):
    username = str(request.user)
    room_details = Room.objects.get(name=room)
    return render(request, 'accounts/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    jsonResponse=json.loads(request.body)
    room = jsonResponse['room_name']
    username = str(request.user)

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

class Sell_Delete(DeleteView):
    model = Sell
    success_url = reverse_lazy('accounts:home')

'''class Sell_Update(UpdateView):
    model = Sell
    fields = ['name', 'description', 'photo', 'price']
    success_url = reverse_lazy('accounts:home')'''
    

class Sell_Update(UpdateView):
    model = Sell
    form_class = Sell_form
    initial = {}
    success_url = reverse_lazy('accounts:home')