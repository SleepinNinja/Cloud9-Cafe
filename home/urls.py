from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path('login/', views.login, name = 'login'),
    path('login/register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('user/<str:username>/', views.user_profile, name = 'user_profile'),
    path('user/<str:username>/change_info/', views.change_info, name = 'change_info'),
    path('manage order/<str:order_type>/', views.manage_order , name = 'manage_order'),
    path('cart-counter/', views.cart_counter, name = 'cart_counter'),
    path('register_user/', views.register_user, name = 'register_user'),
    path('username_available/', views.username_available, name = 'username_available'),
    path('reset_password/', views.forgot_password, name = 'forgot_password'),
    path('action/', views.action, name = 'action'),
    path('submit-review/', views.submit_review, name = 'submit_review'),
]

#path('manage order/action', views.action, name = 'action'),
