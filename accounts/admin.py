from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Relation, Profile


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ("from_user", "to_user", "created_at")


class ProfileInline(admin.StackedInline):
    model = Profile
    on_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
