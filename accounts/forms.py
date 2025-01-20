from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    # the wiget is used to hide the passwor
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
