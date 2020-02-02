from django.urls import path
from . import views


urlpatterns = [
    path('panel/manager/list', views.manager_list, name='manager_list'),
    path('panel/manager/del/<int:pk>', views.manager_delete, name='manager_delete'),
]
