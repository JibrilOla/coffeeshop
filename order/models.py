from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(null=True)
    product_name = models.CharField(max_length=200, null=True)
    total = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    quantity = models.PositiveBigIntegerField(null=True)


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    totalx = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    payment_method = models.CharField(max_length=200, null=True)
    products = models.TextField(max_length=200, null=True)
    status=models.CharField(max_length=200, default='In progress')
    date=models.DateTimeField(auto_now_add=True,null=True)

