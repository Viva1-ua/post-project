from django import forms
from post.models import Commentary, Post


class CommentaryCreateForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content", ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "section", "content"]


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "section", "content"]
