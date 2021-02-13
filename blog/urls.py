from mainpage import views
from .views import blog_single
from django.contrib import admin
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('<int:blog_id>/', blog_single, name='blogsingle'),
]
