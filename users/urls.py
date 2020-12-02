from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('login/',
         auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
         name='logout'),

    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/change-password.html'),
         name='change-password'),

    path('reset-password/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/reset-password.html'),
         name='reset-password'),

    path('reset-password-confirm/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/reset-password-confirm.html'),
         name='password_reset_confirm'),

    path('reset-password-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/reset-password-done.html'),
         name='password_reset_done'),

]
