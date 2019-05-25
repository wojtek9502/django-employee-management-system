from django.urls import path

from ems_app import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('projects/', views.ProjectsView.as_view(), name='projects_list')
]

