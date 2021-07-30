from .models import *
from django import forms

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','picture','preowned','price','condition','category']