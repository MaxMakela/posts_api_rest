from django.contrib import admin
from django.urls import path
from .views import PostView, LoginView, UserCreate, Like

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', PostView.as_view()),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('like/<int:pk>', Like.as_view(), name='like'),
]