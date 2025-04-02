from django.urls import path
from post.views import index

from post.views import FieldListView, FieldDetailView


app_name = "post"

urlpatterns = [
    path("", index, name="home-page"),
    path("fields/", FieldListView.as_view(), name="field-list"),
    path("fields/<int:pk>/", FieldDetailView.as_view(), name="field-detail"),
]
