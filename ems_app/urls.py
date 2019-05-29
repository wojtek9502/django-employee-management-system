from django.urls import path

from ems_app import views

app_name = 'ems_app'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects_list'),
    path('projects/new_project/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_update'),
]

