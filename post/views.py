from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView , UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django import forms
from .models import Product
# Create your views here.


class ProductList(ListView):
	model = Product
	context_object_name = 'products'
	template_name = 'post/product_list.html'

class ProductDetail(DetailView):
	model = Product
	context_object_name = 'product'
	template_name = 'post/product_detail.html'

class ProductCreate(LoginRequiredMixin,CreateView):
	model = Product
	fields = "__all__"
	success_url = reverse_lazy('products')
	template_name = 'post/product_create.html'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(ProductCreate , self).form_valid(form)

class ProductEdit(UpdateView):
	model = Product
	fields = "__all__"
	success_url = reverse_lazy('products')
	template_name = 'post/product_create.html'

class DeleteProduct(DeleteView):
	model = Product
	context_object_name = 'product'
	success_url = reverse_lazy('products')
	template_name ='post/product_conform_delete.html'

class Fridge(ProductList):
	template_name = 'post/includes/fridge.html'

class Laptop(ProductList):
	template_name = 'post/includes/laptop.html'

class Microoven(ProductList):
	template_name = 'post/includes/microoven.html'

class Stove(ProductList):
	template_name = 'post/includes/stove.html'