from django.urls import path
from . import views


urlpatterns = [
    path('comment/add/news/<int:pk>', views.comment_add, name='comment_add'),
    path('panel/comments/list/', views.comment_list, name='comments_list'),
    path('panel/comment/delete/<int:pk>', views.comment_delete, name='comment_delete'),
    path('panel/comment/confirm/<int:pk>', views.comment_confirm, name='comment_confirm'),
]
