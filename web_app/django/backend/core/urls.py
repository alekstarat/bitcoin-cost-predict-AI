from django.urls import path

from . import views

urlpatterns = [
    path('csrf/', views.get_csrf, name='core-csrf'),
    path('login/', views.login_view, name='core-login'),
    path('logout/', views.logout_view, name='core-logout'),
    path('session/', views.session_view, name='core-session'),
    path('whoami/', views.whoami_view, name='core-whoami'),
]