from django.contrib.auth.models import User
from django.db import models

from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ucomment")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="pcomment")
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="rcomment")
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} has commented {self.body[:40]}."
