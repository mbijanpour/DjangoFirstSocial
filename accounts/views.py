from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserLoginForm
from posts.models import Post
from .models import Relation


class UserRegisterView(View):
    # this is to avoid the reusability of the form in the functions if the form got changed
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        """
        the dispatch method in class based views is executed before all the 
        other methods in the class (get,post,...).
        This is used to check if the user is already logged in or not.
        so it prevent the user to access the login or register page again.
        """
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

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
        # on the fields it needs (the browser validation is off from the register html)
        # the passed form is the form with the error messages
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

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
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
            else:
                messages.error(
                    request,
                    'Invalid username or password',
                    extra_tags='alert alert-danger')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)  # the user is in the request object
        messages.success(
            request, 'Logout successful',
            extra_tags='alert alert-success')
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        is_following = False
        print("request=>", request)
        # the pk look for the primary key in the database wether its id or something else
        user = get_object_or_404(User, pk=user_id)
        # posts = Post.objects.filter(user=user)
        posts = user.posts.all()  # with related_name
        relation = Relation.objects.filter(
            from_user=request.user, to_user=user)
        if relation.exists():
            is_following = True
        return render(request, 'accounts/profile.html', {'user': user, 'posts': posts, 'is_following': is_following})


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    # we wait for the evaluation to complete so we use lazy
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class UserPasswordResetDone(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        relation = Relation.objects.filter(
            from_user=request.user, to_user=user).exists()
        if relation:
            messages.warning(request, 'You have already followed this user!')
        else:
            Relation.objects.create(from_user=request.user, to_user=user)
            messages.success(request, "You have followed this user.")
        return redirect('accounts:user_profile', user_id)


class UserUnfollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        relation = Relation.objects.filter(
            from_user=request.user, to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request, "You unfollow this user.")
        else:
            messages.warning(request, "You didn't follow this user.")
        return redirect('accounts:user_profile', user_id)
