from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from accounts.models import UserAccount
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('products')



condition_list = (("Good","Good") , ("Fair","Fair" ) , ("Not Good","Not Good"))

class Product(models.Model):
    user = models.ForeignKey(UserAccount , on_delete=CASCADE)#user has many products 
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to = 'images/',blank=True, null = True)
    preowned = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    condition = models.CharField(max_length=50,choices=condition_list,default='Good')
    category = models.ForeignKey(Category , on_delete=CASCADE)# category has many 
    

    def __str__(self):
	    return self.name

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url
