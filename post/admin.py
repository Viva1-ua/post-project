from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from post.models import Commentary, Post, User, Followers, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("topic", "publisher", "created_at", )
    search_fields = ("topic", "publisher", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at", )
    search_fields = ("author", "post", )


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "date_joined", )
    search_fields = ("username", )
    list_filter = ("email", "date_joined", )


@admin.register(Followers)
class FollowersAdmin(admin.ModelAdmin):
    list_display = ("user", "followers", )


