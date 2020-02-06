from django.urls import path
from . import views


urlpatterns = [
    path(r'^comment/add/news/(?P<pk>\d+)$', views.comment_add, name='comment_add'),
]
