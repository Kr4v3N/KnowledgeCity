from django.urls import path
from . import views


urlpatterns = [
    path('panel/manager/list', views.manager_list, name='manager_list'),
]
