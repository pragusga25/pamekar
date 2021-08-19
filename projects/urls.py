from django.urls import path
from . import views

urlpatterns = [
  path('projects/', views.projects, name='projetcs'),
    path('project/', views.project, name='project'),
]
