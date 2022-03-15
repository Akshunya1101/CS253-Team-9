from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	context = {}
	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def buy(request):
	context = {}
	return render(request, 'accounts/buy.html', context)

@login_required(login_url='login')
def sell(request):
	context = {}
	return render(request, 'accounts/sell.html', context)

@login_required(login_url='login')
def rent(request):
	context = {}
	return render(request, 'accounts/rent.html', context)

@login_required(login_url='login')
def productview(request):
	return HttpResponse("We are at Product View page.")

@login_required(login_url='login')
def checkout(request):
	return HttpResponse("We are at Checkout page.")