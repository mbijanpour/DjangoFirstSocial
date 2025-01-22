from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(View):
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
            User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password1'])
            messages.success(
                request, 'Account created successfully',
                extra_tags='alert alert-success')
            return redirect('home:home')
        # if the form is not valid then it will render the form again but with the error messages
        # on the fields it needs (the browesr validation is off from the register html)
        # the passed form is the form with the error messages
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts\login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'Login successful',
                    extra_tags='alert alert-success')
                return redirect('home:home')
            else:
                messages.error(
                    request,
                    'Invalid username or password',
                    extra_tags='alert alert-danger')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)  # the user is in the request object
        messages.success(
            request, 'Logout successful',
            extra_tags='alert alert-success')
        return redirect('home:home')
