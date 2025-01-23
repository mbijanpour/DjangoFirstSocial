from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=(self.id, self.slug))
