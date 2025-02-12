from django.contrib.auth.models import User
from django.db import models


class Relation(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} followed {self.to_user} at {self.created_at}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
