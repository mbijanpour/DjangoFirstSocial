from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')
