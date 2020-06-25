from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from json import JSONEncoder
from django.core.validators import ValidationError, RegexValidator
import re

def validate_name(value):
    pattern = re.compile("[a-zA-Z][a-zA-Z \.]+[a-zA-Z]$")
    if pattern.match(value):
        return value
    else:
        raise ValidationError('Must have only characters or space or period')
	


class RegisterUser(models.Model):
    user_name = models.CharField(max_length=100,  validators=[
        RegexValidator(
            regex='^[a-zA-Z][a-zA-Z \.]+[a-zA-Z]$',
            message='Username must not conatain numbers or characters',
            code='invalid_username'
        ),
    ])
    user_mobile_no = models.CharField(max_length=40,validators=[
        RegexValidator(
            regex='^[0-9]$',
            message='Mobile number must  conatain only numbers',
            code='invalid_mobileno'
        ),
    ])
    user_passport_no = models.CharField(max_length=40)
    user_dob = models.DateField(blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_password = models.CharField(max_length=100, blank=True, null=True)
    user_image = models.ImageField( blank=True)

class RegiseterUserEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

