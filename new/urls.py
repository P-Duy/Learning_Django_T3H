from django.urls import path
from . import views

app_name = "new"
urlpatterns = [
    path("", views.new_view, name="new"),
    path("new/<int:pk>/", views.new_post, name="new_post"),
]
