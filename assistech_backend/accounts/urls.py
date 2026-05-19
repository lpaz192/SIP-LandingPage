from django.urls import path
from . import views

urlpatterns = [
    path('',           views.landing_view,  name='assistech-landing'),
    path('login/',     views.login_view,     name='login'),
    path('logout/',    views.logout_view,    name='logout'),
    path('register/',  views.register_view,  name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]