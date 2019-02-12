from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    #add an email field to the registration
    email = forms.EmailField() #default equals to true

    class Meta:
        model = User #the model that will be effected within the form
        fields = ['username','email','password1','password2'] #the display order


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] #let the form know those are the fields we want to work with


class ProfileUpdateForm(forms.ModelForm):#since profile is a seperate table connected by one to one relationship
    class Meta:
        model = Profile
        fields=['image']

