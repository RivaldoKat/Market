from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django import forms
from .models import Category, Product
from .forms import ProductForm
# Create your views here.


class ProductList(ListView):
	template_name = 'posts/product_list.html'
	model = Product
	context_object_name = 'products'

class ProductCreate(LoginRequiredMixin,CreateView):
	model = Product
	fields = ['name','picture','preowned','price','condition','category']
	success_url = reverse_lazy('posts:products')

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(ProductCreate , self).form_valid(form)


class ProductDetail(DetailView):
	model = Product
	context_object_name = 'categories'
	template_name = 'posts/product_detail.html'



	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(ProductCreate , self).form_valid(form)

class ProductEdit(UpdateView):
	model = Product
	fields = ['name','condition','category','price']
	success_url = reverse_lazy('products:products')
	template_name = 'posts/product_form.html'

class DeleteProduct(DeleteView):
	model = Product
	context_object_name = 'product'
	success_url = reverse_lazy('posts:products')
	template_name ='posts/product_conform_delete.html'

class CategoryListView(ListView):
	model 	= Category
	context_object_name = 'categories'
	template_name = 'posts/category_list.html'

class CategoryDetail(DetailView):
	model = Category
	context_object_name = 'categories'
	template_name = 'posts/category_detail.html'