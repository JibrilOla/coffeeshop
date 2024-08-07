from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_placed = models.DateTimeField(auto_now_add=True, null=True)
    persons = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
