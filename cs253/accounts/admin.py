from django.contrib import admin
from .models import Sell
from .models import Room
from .models import Message
# from .models import Customer, Seller, Order

admin.site.register(Sell)
admin.site.register(Room)
admin.site.register(Message)
# admin.site.register(Customer)
# admin.site.register(Seller)
# admin.site.register(Order)