from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name = "menu"),
    path('item/add-item/', views.add_item, name = 'add_item'),
    path("<str:type>/", views.menu_display, name = 'menu_display'),
]
