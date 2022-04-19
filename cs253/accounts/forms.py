from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Sell

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
  

class Sell_form(ModelForm):
	class Meta:
		model = Sell
		fields = ['name', 'description', 'photo', 'price']

