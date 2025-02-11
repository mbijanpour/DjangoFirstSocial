from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostCreateUpdateForm, CommentCreateForm
from home.models import Comment


class PostDetailView(View):
    form_class = CommentCreateForm

    def setup(self, request, *args, **kwargs):
        # the parameters which passed in the url will save in kwargs
        # we set it to post instance so that django wont confuse it with model Post
        self.post_instance = get_object_or_404(
            Post, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return super().setup(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # post = get_object_or_404(Post, pk=post_id, slug=post_slug)
        comments = self.post_instance.pcomment.filter(is_reply=False)
        return render(request, "posts/detail.html", {"post": self.post_instance, "comments": comments, "form": self.form_class})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.post_instance
            new_comment.save()
            messages.success(
                request, "your comment submitted successfully.", 'success')
            return redirect('posts:post_detail', self.post_instance.id, self.post_instance.slug)


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user.id == request.user.id:
            try:
                post.delete()
                messages.success(
                    request,
                    "Post deleted successfully",
                    extra_tags="alert alert-success",
                )
            except:
                messages.error(
                    request,
                    "Post could not be deleted",
                    extra_tags="alert alert-danger",
                )
        else:
            messages.error(
                request,
                "You are not allowed to delete this post",
                extra_tags="alert alert-danger",
            )
        return redirect("home:home")


class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm

    def setup(self, request, *args, **kwargs):
        """
        Considering that the setup will execute before dispatch
        we connect to the db here and then use it in different methods
        in order to reduce the times we connect to the db.
        """
        self.post_instance = get_object_or_404(
            Post, pk=kwargs["post_id"]
        )  # we store post in self to have access to it from different methods
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(
                request,
                "You are not allowed to update this post",
                extra_tags="alert alert-danger",
            )
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, post_id):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, "posts/update.html", {"form": form})

    def post(self, request, post_id):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.slug = slugify(updated_post.slug)
            updated_post.save()
            messages.success(
                request, "Post updated successfully", extra_tags="alert alert-success"
            )
            return redirect("posts:post_detail", post_id=post.id, post_slug=post.slug)
        else:
            messages.error(
                request, "Post could not be updated", extra_tags="alert alert-danger"
            )
            return render(request, "posts/update.html", {"form": form})


class PostCreateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm

    def get(self, request):
        form = self.form_class()
        return render(request, "posts/create.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.slug = slugify(new_post.slug)
            new_post.save()
            messages.success(
                request, "Post created successfully", extra_tags="alert alert-success"
            )
            return redirect("posts:post_detail", new_post.id, new_post.slug)
