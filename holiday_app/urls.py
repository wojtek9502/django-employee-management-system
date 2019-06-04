from django.urls import path
from holiday_app import views

app_name = 'holiday_app'

urlpatterns = [
    path('show/', views.HolidayListView.as_view(), name='holidays_list'),
    path('new_holiday/', views.HolidayCreateView.as_view(), name='holiday_create'),
    # path('<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    # path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    # path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_update'),
]
