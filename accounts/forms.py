from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'john doe'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johnDoe@gmail.com'}))
    # the wiget is used to hide the passwor
    # the attrs is used to add a class to the input field
    # this is for html/css classes hwich used to add a bootstrap class to the input field
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'confirm password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username

    def clean(self):
        cd = super().clean()
        password1 = cd.get('password1')
        password2 = cd.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'john doe'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))
