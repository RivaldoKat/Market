from .models import *
from django import forms


choice_list = (("Good","Good") , ("Fair","Fair" ) , ("Not Good","Not Good"))

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','picture','preowned','price','condition','category']


		widgets = { 'name' : forms.TextInput(attrs={'class': 'form-control'}),
			'price' : forms.TextInput(attrs={'class': 'form-control'}),
			'condition' : forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
			'preowned' : forms.CheckboxInput(attrs={'class': 'form-control'}),
            # 'picture': forms.ImageField(attrs={'class': 'form-control'})
		}