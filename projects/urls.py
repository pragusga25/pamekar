from django.urls import path
from . import views

urlpatterns = [
  path('', views.projects, name='projetcs'),
    path('project/<int:pk>', views.project, name='project'),
]
