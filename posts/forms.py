from django import forms

from . import models
from home.models import Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ("slug", "body")
        help_texts = {
            "slug": "write the slug as the example: my-post-slug",
            "body": "The content of the post",
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={'class': 'form-control',
                                          'rows': 3,
                                          'placeholder': 'Write your comment here'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={'class': 'form-control',
                                          'rows': 2,
                                          'placeholder': 'Write your Reply here'})
        }
