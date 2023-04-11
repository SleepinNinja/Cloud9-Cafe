from django.urls import path
from . import views

urlpatterns = [
    path("", views.chefs, name = "chefs"),
]
