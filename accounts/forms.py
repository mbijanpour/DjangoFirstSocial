from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'john doe'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johnDoe@gmail.com'}))
    # the wiget is used to hide the passwor
    # the attrs is used to add a class to the input field
    # this is for html/css classes hwich used to add a bootstrap class to the input field
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'confirm password'}))
