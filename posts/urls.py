from django import urls
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns =[
	path('',ProductList.as_view(),name="products"),
	path('create/',ProductCreate.as_view(),name="create"),
	path('product/<int:pk>/',ProductDetail.as_view(),name="product_detail"),
	path('product_edit/<int:pk>/',ProductEdit.as_view(),name="product_edit"),
	path('product_delete/<int:pk>/',DeleteProduct.as_view(),name="product_delete"),

	# Category urls

	path('category_list',CategoryListView.as_view(),name='categories'),
	path('category/<int:pk>',CategoryDetail.as_view(),name='category'),
	
	
]

if settings.DEBUG:
	urlpatterns  += static(settings.MEDIA_URL,
	document_root = settings.MEDIA_ROOT)