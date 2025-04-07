from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from post.forms import CommentaryForm
from post.models import Post, User, Field, Section, Commentary


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


def post(request, *args, **kwargs):
    form = CommentaryForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy("post:field-list"))


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post_object = get_object_or_404(Post, pk=self.kwargs["pk"])
        if request.method == "POST":
            form = CommentaryForm(request.POST)
            if form.is_valid():
                comments = form.save(commit=False)
                comments.author = self.request.user
                comments.post = post_object
                comments.save()
                return redirect("post:post-detail", pk=post_object.pk)
            form = CommentaryForm()
