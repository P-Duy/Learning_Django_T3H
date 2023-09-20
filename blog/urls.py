from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<int:pk>/", views.post, name="post"),
    path("post_add/", views.post_add, name="post_add"),
    path("post_edit/<int:pk>/", views.post_edit, name="post_edit"),
    path("post_delete/<int:pk>/", views.post_delete, name="post_delete"),
]
