from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('plot/', views.plot, name='plot'),
    path('plot_eq_fields/', views.plot, name='plot_eq_fields'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_registration/', views.user_registration, name='user_registration'),
]