from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('buy/', views.buy, name="buy"),
	path('sell/', views.sell, name="sell"),
	path('rent/', views.rent, name="rent"),
	path('productview/', views.productview, name="ProductView"), # To view details of any available product
	path('checkout/', views.checkout, name="CheckOut"),  
]