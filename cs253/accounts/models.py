from django.db import models
from datetime import datetime
# Create your models here.

class Sell(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    photo = models.ImageField(null=True,blank=True,upload_to="images/")
    price = models.IntegerField()

    def __str__(self):
        return f"Item name is {self.name} and it costs Rs {self.price}."

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
