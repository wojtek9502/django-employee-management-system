from django.urls import path
from resources_app import views

app_name = 'resources_app'

urlpatterns = [
    path('show/', views.ResourceListView.as_view(), name='resources_list'),
    path('new_resource/', views.ResourceCreateView.as_view(), name='resource_create'),
    # path('<int:pk>', views.ResourceDetailView.as_view(), name='resource_detail'),
    # path('<int:pk>/delete/', views.ResourceDeleteView.as_view(), name='resource_delete'),
    # path('<int:pk>/edit/', views.ResourceUpdateView.as_view(), name='resource_update'),
]
