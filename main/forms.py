from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
	widgets = {
	    'username': forms.EmailInput,
	}
        help_texts = {
            'username': ''
        }
        labels = {
            'username': 'Email'
        }
