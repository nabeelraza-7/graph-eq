from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('plot/', views.plot, name='plot'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_registration/', views.user_registration, name='user_registration'),
]