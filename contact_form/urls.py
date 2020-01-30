from django.urls import path
from . import views


urlpatterns = [
    path('contact/submit', views.contact_add, name='contact_add'),
    path('panel/contact-form', views.contact_show, name='contact_show'),
    path('panel/contact-form/<int:pk>', views.contact_delete, name='contact_delete'),

]
