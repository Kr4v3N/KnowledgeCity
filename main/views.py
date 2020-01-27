from django.shortcuts import render, get_object_or_404, redirect

from category.models import Category
from .models import Main
from news.models import News
from subcategory.models import SubCategory


def home(request):
    site = Main.objects.get(pk=3)
    news = News.objects.all().order_by('-pk')
    category = Category.objects.all()
    subcat = SubCategory.objects.all()

    return render(request, 'home.html', {'site': site,
                                         'news': news,
                                         'category': category,
                                         'subcat': subcat
                                         })


def about(request):
    site = Main.objects.get(pk=3)
    news = News.objects.all().order_by('-pk')
    category = Category.objects.all()
    subcat = SubCategory.objects.all()

    return render(request, 'front/about.html', {'site': site,
                                                'category': category,
                                                'subcat': subcat,
                                                'news': news,
                                                })


def panel(request):
    return render(request, 'back/admin_home.html')
