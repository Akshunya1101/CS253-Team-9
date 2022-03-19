from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
        name = models.CharField(max_length=100,null=True)
        user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
        date_created = models.DateTimeField(auto_now_add=True)
        phone = models.IntegerField(default=0)

        def __str__(self):
            return self.name

class Seller(models.Model):
        name = models.CharField(max_length=100,null=True)
        user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
        date_created = models.DateTimeField(auto_now_add=True)
        phone = models.IntegerField(default=0)

        def __str__(self):
            return self.name

class Sell(models.Model):
    name = models.CharField(max_length=40,null=True)
    description = models.TextField(max_length=200,null=True)
    photo = models.ImageField(null=True,blank=True,upload_to="images/")
    price = models.IntegerField()
    seller = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.OneToOneField(Sell,null=True,on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
