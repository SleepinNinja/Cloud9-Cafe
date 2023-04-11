from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem
from datetime import datetime
# Create your models here.


class Cart(models.Model):
    checked_out = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


class Order(models.Model):
    order_date = models.DateTimeField(default = datetime.now)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete = models.DO_NOTHING, primary_key = False)
    status = models.CharField(max_length = 10000, default = 'unordered')
    total_price = models.IntegerField(default = 0)
    delivery_time = models.IntegerField(default = 0)
    otp = models.IntegerField(default = 0)


class CartItem(models.Model):
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
