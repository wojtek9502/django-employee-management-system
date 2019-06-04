from django.urls import path
from project_app import views

app_name = 'project_app'

urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='projects_list'),
    path('projects/new_project/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_update'),
]

