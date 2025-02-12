from django.contrib import admin
from .models import Post, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("slug", "user", "created_at", "updated_at")
    search_fields = ("slug", "user__username")
    list_filter = ("created_at", "user__username")
    raw_id_fields = ("user",)
    prepopulated_fields = {"slug": ("body",)}


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "post")
    search_fields = ("user__username", "post__slug")
