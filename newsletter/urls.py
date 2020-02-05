from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/add', views.news_letter, name='news_letter'),
    path('panel/newsletter/emails', views.news_emails, name='news_emails'),
    path('panel/newsletter/del/<int:pk>', views.news_emails_delete, name='news_emails_delete'),
]