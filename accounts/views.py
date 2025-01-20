from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm


class RegisterView(View):
    # this is to avoid the reusability of the form in the functions if the form got changed
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            password1 = cd['password1']
            password2 = cd['password2']
            if password1 == password2:
                User.objects.create_user(
                    username=cd['username'],
                    email=cd['email'],
                    password=password1)
                messages.success(
                    request, 'Account created successfully',
                    extra_tags='alert alert-success')
                return redirect('home:home')
            else:
                messages.error(
                    request, 'Passwords do not match',
                    extra_tags='alert alert-danger')
        # if the form is not valid then it will render the form again but with the error messages
        # on the fields it needs (the browesr validation is off from the register html)
        # the passed form is the form with the error messages
        return render(request, self.template_name, {'form': form})
