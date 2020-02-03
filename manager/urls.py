from django.urls import path
from . import views

urlpatterns = [
    path('panel/manager/list', views.manager_list, name='manager_list'),
    path('panel/manager/group', views.manager_group, name='manager_group'),
    path('panel/manager/group/add', views.manager_group_add, name='manager_group_add'),
    path('panel/manager/group/del/<str:name>', views.manager_group_delete, name='manager_group_delete'),
    path('panel/manager/del/<int:pk>', views.manager_delete, name='manager_delete'),
    path('panel/manager/group/show/<int:pk>', views.users_groups, name='users_groups'),
    path('panel/manager/group/addtogroup/<int:pk>', views.add_users_to_groups, name='add_users_to_groups'),
    path('panel/manager/group/delgroup/<int:pk>/<str:name>', views.del_users_to_groups, name='del_users_to_groups'),
    path('panel/manager/perms', views.manager_perms, name='manager_perms'),
    path('panel/manager/perms/del/<str:name>', views.manager_perms_del, name='manager_perms_del'),
    path('panel/manager/perms/add', views.manager_perms_add, name='manager_perms_add'),
]


