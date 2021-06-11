from django.contrib import admin
from django.urls import path,include
from .views import ProductList,ProductDetail,ProductCreate,ProductEdit,DeleteProduct,Fridge,Laptop,Microoven,Stove

from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
	path('',ProductList.as_view(),name="products"),
	path('product/<int:pk>/',ProductDetail.as_view(),name="product_detail"),
	path('product_create/',ProductCreate.as_view(), name='product_create'),
	path('product_edit/<int:pk>/',ProductEdit.as_view(),name="product_edit"),
	path('product_delete/<int:pk>/',DeleteProduct.as_view(),name="product_delete"),
	path('product/fridge',Fridge.as_view(),name="fridge"),
	path('product/laptop',Laptop.as_view(),name="laptop"),
	path('product/microven',Microoven.as_view(),name="micro"),
	path('product/stoves',Stove.as_view(),name="stove"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    Fridge


