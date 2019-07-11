from django.urls import path
from entrance_exit_app import views

app_name = 'entrance_exit_app'

urlpatterns = [
    path('show/', views.EntranceExitListView.as_view(), name='entrance_exit_list'),
    # path('new_holiday/', views.HolidayCreateView.as_view(), name='holiday_create'),
    # path('<int:pk>', views.HolidayDetailView.as_view(), name='holiday_detail'),
    # path('<int:pk>/delete/', views.HolidayDeleteView.as_view(), name='holiday_delete'),
    # path('<int:pk>/edit/', views.HolidayUpdateView.as_view(), name='holiday_update'),
]
