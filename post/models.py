from django.contrib.auth.models import AbstractUser
from django.db import models


class Field(models.Model):
    field = models.CharField(max_length=55, unique=True)

    class Meta:
        ordering = ["field", ]
        verbose_name = "Field"


class Topic(models.Model):
    name = models.ForeignKey(
        "Field",
        max_length=55,
        unique=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", ]
        verbose_name = "Topic"


class Post(models.Model):
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    content = models.TextField()
    publisher = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ["-created_at", "topic", ]
        verbose_name = "Post"


class Commentary(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    author = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Commentarie"


class User(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username", ]
        verbose_name = "User"


class Followers(models.Model):
    followers = models.ForeignKey(
        "User", on_delete=models.CASCADE,
        related_name="followers"
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE,
        related_name="following_user",
        verbose_name="Following"
    )

    class Meta:
        verbose_name = "Follower"
