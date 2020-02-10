from django.urls import path
from . import views


urlpatterns = [
    path('blacklist', views.black_list, name='black_list'),
]
