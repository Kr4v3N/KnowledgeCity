from django.shortcuts import render, get_object_or_404, redirect

from category.models import Category
from .models import Main
from news.models import News


def home(request):
    site = Main.objects.get(pk=3)
    news = News.objects.all().order_by('-pk')
    category = Category.objects.all()

    return render(request, 'home.html', {'site': site,
                                         'news': news,
                                         'category': category
                                         })


def about(request):
    site = Main.objects.get(pk=3)
    category = Category.objects.all()

    return render(request, 'front/about.html', {'site': site,
                                                'category': category
                                                })


def panel(request):
    return render(request, 'back/admin_home.html')
