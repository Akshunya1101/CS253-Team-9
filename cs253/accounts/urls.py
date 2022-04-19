from django.urls import path
from . import views
from .views import (Sell_Create,Sell_List,Sell_Details,Sell_Delete, Sell_Update)
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('buy/',login_required(Sell_List.as_view()), name="buy"),
	path('search/',views.search, name="search"),
	path('sell/',views.Sell_Create, name="sell"),
	path('sell_detail/<int:pk>',Sell_Details.as_view(), name="item_details"),
	path('rent/', views.rent, name="rent"), 
	path('enterRoom/', views.enterRoom, name="enterRoom"), 
	path('<str:room>/', views.room, name='room'),
    path('enterRoom/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
	path('delete/<int:pk>', Sell_Delete.as_view(), name='delete_item'),
	path('update/<int:pk>', Sell_Update.as_view(), name='update_item'),
]