from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'username1','id':'username1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','id':'login-password1'}))
    


