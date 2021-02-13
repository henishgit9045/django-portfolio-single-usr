from .views import project
from django.contrib import admin
from django.urls import path

app_name = 'projects'
urlpatterns = [
    path('<int:project_id>/', project, name='project_details'),
]
