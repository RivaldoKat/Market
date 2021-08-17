from django.conf.urls import url
from django.urls import path
from .views import *

app_name = "accounts"
# This is a namespace used inside templates 

urlpatterns=[
    path('registration/',UserRegisterView.as_view(),name="register"),
    path('login/',CustomLoginView.as_view(),name="login"),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('payment/', PaymentView.as_view(), name='payment')
]