from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from post.models import Post, User, Field


@login_required
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_field": Post.objects.all().count(),
        "num_users": User.objects.count(),
    }

    return render(request, "post/index.html", context=context)


class FieldListView(generic.ListView):
    model = Field
    template_name = "post/field_list.html"
    success_url = reverse_lazy("post:field-list")


class FieldDetailView(generic.DetailView):
    model = Field
