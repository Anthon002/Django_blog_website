from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django import forms

class CreationUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CreatePost(ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=['likes']

class CreateComment(ModelForm):
    class Meta:
        model=Comment
        fields="__all__"
        exclude=['user']



class SettingsForm(ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic']
        exclude=['user']

class UsernameForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username"]
        