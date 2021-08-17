from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from .models import UserAccount

# Create your views here.

class UserRegisterView(generic.FormView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts:products')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(UserRegisterView, self).form_valid(form)

    def get(self , *args , **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts:products')
        return super(UserRegisterView,self).get(*args,**kwargs)

class CustomLoginView(LoginView):
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('posts:products')
    
class UserEditView(generic.UpdateView):
    model = UserAccount
    template_name = 'accounts/edit_profile.html'
    fields = ['first_name', 'last_name', 'email', 'cellphone']
    success_url = reverse_lazy('posts:products')

    def get_object(self):
        return self.request.user

class ProfileView(generic.DetailView):
    model = UserAccount
    context_object_name = 'user'
    def form_valid(self,form):
	    form.instance.user = self.request.user
	    return super(ProfileView , self).form_valid(form)

class PaymentView(generic.View):
	def get(self,*args, **kwargs):
		return render(self.request, "accounts/payment.html")