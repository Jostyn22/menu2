from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página de bienvenida
    path('', views.welcome, name='welcome'),

    # Registro, login, logout, dashboard
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/index.html', views.dashboard_view, name='dashboard_index'),
    path('dashboard/index2.html', views.index2_view, name='index2'),
    path('dashboard/index3.html', views.index3_view, name='index3'),

    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
