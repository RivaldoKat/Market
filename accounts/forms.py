from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
Usermodel = get_user_model()
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cellphone = forms.CharField(max_length = 15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta: 
        model = Usermodel
        fields = ('first_name', 'last_name', 'email', 'cellphone','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# class EditProfileForm(UserChangeForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     cellphone = forms.CharField(max_length = 15, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     class Meta: 
#         model = Usermodel
#         fields = ('first_name', 'last_name', 'email', 'cellphone')