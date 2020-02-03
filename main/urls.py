from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('panel/setting/', views.site_settings, name='site_settings'),
    path('panel/about/setting/', views.about_settings, name='about_settings'),
    path('contact/', views.contact, name='contact'),
    path('panel/change/pass', views.change_pass, name='change_pass'),
]
