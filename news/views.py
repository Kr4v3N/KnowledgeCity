from django.shortcuts import render
from .models import News
from main.models import Main


# Create your views here.


def news_detail(request, pk):

    site = Main.objects.get(pk=3)
    news = News.objects.filter(pk=pk)

    return render(request, 'front/news_detail.html', {'news': news, 'site': site})
