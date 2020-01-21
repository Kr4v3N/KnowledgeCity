from django.shortcuts import render
from .models import News
from main.models import Main


# Create your views here.


def news_detail(request, pk):
    site = Main.objects.get(pk=3)
    news = News.objects.filter(pk=pk)

    return render(request, 'front/news_detail.html', {'news': news, 'site': site})


def news_list(request):
    news = News.objects.all()

    return render(request, 'back/news_list.html', {'news': news})


def news_add(request):
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newstxtshort = request.POST.get('newstxtshort')
        newstext = request.POST.get('newstext')

        if newstitle == "" or newstext == "" \
                or newstxtshort == "" \
                or newscategory == "" \
                or newstitle == "":
            error = "Tous les champs sont requis"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html')
