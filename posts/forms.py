from django import forms

from . import models


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ("slug", "body")
        help_texts = {
            "slug": "write the slug as the example: my-post-slug",
            "body": "The content of the post",
        }
