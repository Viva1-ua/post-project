from django.urls import path
from post.views import index, PostCreateView, PostUpdateView

from post.views import (FieldListView, FieldDetailView,
                        PostDetailView, SectionDetailView,
                        PostDeleteView, PublisherPostListView,
                        UserAccountListView)


app_name = "post"

urlpatterns = [
    path("", index, name="home-page"),
    path("fields/", FieldListView.as_view(), name="field-list"),
    path("fields/<int:pk>/", FieldDetailView.as_view(), name="field-detail"),
    path("section/<int:pk>/", SectionDetailView.as_view(), name="section-detail"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
    path("post/publisher-posts/", PublisherPostListView.as_view(), name="publisher-post-list"),
    path("post/user-account/<int:pk>/", UserAccountListView.as_view(), name="user-account-list"),
]
