from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from post.models import Post, User, Field, Section


admin.site.register(Field)
admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "publisher",
        "created_at",
    )
    search_fields = ("publisher", )
    list_filter = ("created_at", )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "field",
    )
    search_fields = ("name", )
    list_filter = ("name", )


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "date_joined",
    )
    search_fields = ("username", )
    list_filter = ("username", )

