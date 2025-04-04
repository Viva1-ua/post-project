from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from post.models import Post, User, Field, Section


@login_required
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_field": Field.objects.count(),
        "num_users": User.objects.count(),
        "num_posts": Post.objects.count(),
    }

    return render(request, "post/index.html", context=context)


class FieldListView(generic.ListView):
    model = Field
    template_name = "post/field_list.html"
    success_url = reverse_lazy("post:field-list")


class FieldDetailView(generic.DetailView):
    model = Field


class SectionDetailView(generic.DetailView):
    model = Section


class PostDetailView(generic.DetailView):
    model = Post
