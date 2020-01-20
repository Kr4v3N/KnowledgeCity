from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News


# Create your views here.

def home(request):
    site = Main.objects.get(pk=3)
    news = News.objects.all()

    return render(request, 'home.html', {'site': site, 'news': news})


def about(request):
    site = Main.objects.get(pk=3)

    return render(request, 'front/about.html', {'site': site})


def panel(request):

    return render(request, 'back/admin_home.html')
