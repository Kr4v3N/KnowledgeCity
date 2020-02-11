from django.urls import path
from . import views


urlpatterns = [
    path('panel/category/list', views.category_list, name='category_list'),
    path('panel/category/add', views.category_add, name='category_add'),
    path('export/category/csv', views.export_cat_csv, name='export_cat_csv'),
    path('import/category/csv', views.import_cat_csv, name='import_cat_csv'),
]
