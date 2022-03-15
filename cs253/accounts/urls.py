from django.urls import path
from . import views
from .views import Sell_Create
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('buy/', views.buy, name="buy"),
	path('sell/',Sell_Create.as_view(), name="sell"),
	path('rent/', views.rent, name="rent"),
    path('', views.home, name="home"),
]