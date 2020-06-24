from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    full_name = forms.CharField(max_length=32)
    mobile_no = forms.CharField(max_length=10,min_length=10)
    image = forms.ImageField(required=False)
    passport_num = forms.CharField()
    dob=forms.DateField
    email=forms.EmailInput
    age = forms.IntegerField(min_value=16)
  
class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.PasswordInput()