from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import ValidationError, RegexValidator


class SignUpForm(forms.Form):
    full_name = forms.CharField(max_length=32,validators=[
        RegexValidator(
            regex='^[a-zA-Z][a-zA-Z \.]+[a-zA-Z]$',
            message='Username must not conatain numbers or characters',
            code='invalid_username'
        ),
    ])
    mobile_no = forms.CharField(max_length=10,min_length=10,validators=[
        RegexValidator(
            regex='^[0-9]+$',
            message='Mobile number must  conatain only numbers',
            code='invalid_mobileno'
        ),
    ])
    image = forms.ImageField()
    passport_num = forms.CharField()
    dob=forms.DateField
    email=forms.EmailInput
    age = forms.IntegerField(min_value=16)
  
class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.PasswordInput()
