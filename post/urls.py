from django.urls import path
from post.views import index

from post.views import (FieldListView, FieldDetailView,
                        PostDetailView, SectionDetailView)


app_name = "post"

urlpatterns = [
    path("", index, name="home-page"),
    path("fields/", FieldListView.as_view(), name="field-list"),
    path("fields/<int:pk>/", FieldDetailView.as_view(), name="field-detail"),
    path("section/<int:pk>/", SectionDetailView.as_view(), name="section-detail"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]
