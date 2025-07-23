from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
    
    password = forms.CharField(widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)