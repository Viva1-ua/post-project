from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from post.forms import CommentaryCreateForm
from post.models import Post, User, Field, Section


@login_required
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_field": Field.objects.count(),
        "num_users": User.objects.count(),
        "num_posts": Post.objects.filter(publisher=request.user).count(),
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


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        post_object = get_object_or_404(Post, pk=self.kwargs["pk"])
        form = CommentaryCreateForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.author = self.request.user
            comments.post = post_object
            comments.save()
            return redirect("post:post-detail", pk=post_object.pk)
        raise ValidationError(form.errors)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "section", "content"]
    template_name = "post/post_form.html"

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post:post-detail", kwargs={"pk": self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ["title", "section", "content"]
    template_name = "post/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher

    def get_success_url(self):
        return reverse_lazy("post:post-detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("post:field-list")
    template_name = "post/post_delete_confirm.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class PublisherPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    success_url = reverse_lazy("post:publisher-post-list")
    template_name = "post/publisher_post_list.html"
    context_object_name = "publisher_posts"

    def get_queryset(self):
        return Post.objects.filter(publisher=self.request.user)


class UserAccountListView(LoginRequiredMixin, generic.ListView):
    model = User

