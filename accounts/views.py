from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import SignUpForm

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'accounts/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('main')
    #     return super(UserRegisterView, self).get(*args,**kwargs)

