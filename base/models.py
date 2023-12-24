from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


# Create your models here.
class Customer(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    rate = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20)
    link = models.URLField()
    img_src = models.URLField()