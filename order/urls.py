from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name = 'order'),
    path('clear/', views.clear, name = 'clear'),
    path('ordered/', views.ordered, name = 'ordered'),
    path('remove/', views.remove_item, name='remove_item')
]
