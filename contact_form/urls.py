from django.urls import path
from . import views


urlpatterns = [
    path('contact/submit', views.contact_add, name='contact_add'),

]
