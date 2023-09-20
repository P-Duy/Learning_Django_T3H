from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path("", views.student_view, name="student"),
    path("detail/<int:pk>/", views.student_detail, name="detail"),
]
