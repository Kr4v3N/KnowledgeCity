from django.urls import path
from . import views


urlpatterns = [
    path('panel/trending', views.trending_add, name='trending_add'),
    path('panel/trending/<int:pk>', views.trending_delete, name='trending_delete'),
    path('panel/trending/edit/<int:pk>', views.trending_edit, name='trending_edit'),
]
