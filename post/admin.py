from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from post.models import (Post, User,
                         Topic, Field)


admin.site.register(Field)
admin.site.unregister(Group)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("topic", "publisher", "created_at", )
    search_fields = ("topic", "publisher", )


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "date_joined", )
    search_fields = ("username", )
    list_filter = ("email", "date_joined", )
