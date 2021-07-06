from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

condition_list = (("Good","Good") , ("Fair","Fair" ) , ("Not Good","Not Good"))
category_list = (("Fridge","Fridge"),("Stove","Stove"),("Laptop","Laptop"),("Microoven","Microoven"))
class Product(models.Model):
	title = models.CharField(max_length=200)
	picture = models.ImageField(upload_to='images',blank=False)
	preowned = models.BooleanField(default=False)
	price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
	condition = models.CharField(max_length=50,choices=condition_list,default='Good')
	category = models.CharField(max_length=50,choices=category_list,default='Fridge')


	def __str__(self):
		return self.title