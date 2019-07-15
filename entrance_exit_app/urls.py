from django.urls import path
from entrance_exit_app import views

app_name = 'entrance_exit_app'

urlpatterns = [
    path('show/', views.EntranceExitListView.as_view(), name='entrance_exit_list'),
    path('new_entrance_exit/', views.EntranceExitCreateView.as_view(), name='entrance_exit_create'),
    path('<int:pk>', views.EntranceExitDetailView.as_view(), name='entrance_exit_detail'),
    path('<int:pk>/delete/', views.EntranceExitDeleteView.as_view(), name='entrance_exit_delete'),
    path('<int:pk>/edit/', views.EntranceExitUpdateView.as_view(), name='entrance_exit_update'),
]
