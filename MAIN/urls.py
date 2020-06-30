from django.urls import path

from .views import *

app_name = 'user'
urlpatterns = [
    path('register/', register_form, name='register'),
    path('logout/', logoutView, name='logout'),
    path('login/', loginView, name='login'),
    path('dashboard/<uuid:uuid>/', dashboardView, name='dashboard'),
]