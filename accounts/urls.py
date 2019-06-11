from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [ #wiazanie widoku z django z templatka login.html
    path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'), #idzie do homepage
    path('signup/', views.register, name='signup'),
    path('after_signup/', views.AfterRegisterPage.as_view(), name="after_signup"),

    path('password_reset/',  
            auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), 
            name='password_reset'
        ),

    path('password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name= "accounts/password_reset_done.html"), 
            name='password_reset_done'
        ),
    
    path('accounts/reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='reset_password_confirm'),

    path('reset/done/',
            auth_views.PasswordResetCompleteView.as_view(template_name= "accounts/password_reset_complete.html"), 
            name='password_reset_complete'
        ),

    path('my_profile/', views.MyProfileTemplateView.as_view(), name='my_profile'),
    path('my_profile_update/<int:pk>/', views.UpdateMyProfileView.as_view(), name='my_profile_update'),


    path('users_list/', views.UsersListView.as_view(), name='users_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user_grant/<int:pk>/', views.UserGrantDetailView.as_view(), name='user_grant'),
    path('user_activate/<int:pk>/', views.UserActivateDetailView.as_view(), name='user_activate'),
    path('user_deactivate/<int:pk>/', views.UserDeactivateDetailView.as_view(), name='user_deactivate'),
    path('get_rights/<int:pk>/', views.UserGetRightsDetailView.as_view(), name='get_rights'),
]  
