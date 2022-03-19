from django.urls import path
from . import views
from .views import (Sell_Create,Sell_List,Sell_Details)
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('buy/',login_required(Sell_List.as_view()), name="buy"),
	path('sell/',login_required(Sell_Create.as_view()), name="sell"),
	path('details/<int:pk>',login_required(Sell_Details.as_view()), name="item_details"),
	path('rent/', views.rent, name="rent"), 
	path('enterRoom/', views.enterRoom, name="enterRoom"), 
	path('<str:room>/', views.room, name='room'),
    path('enterRoom/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]