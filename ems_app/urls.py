from django.urls import path

from ems_app import views

app_name = 'ems_app'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
]

