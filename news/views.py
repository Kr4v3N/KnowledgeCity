from django.shortcuts import render, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage


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
        newstxt = request.POST.get('newstxt')

        if newstitle == "" or newstxt == "" \
                or newstxtshort == "" \
                or newscategory == "" \
                or newstitle == "":
            error = "Tous les champs sont requis"
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fileSystem = FileSystemStorage()
            filename = fileSystem.save(myfile.name, myfile)
            url = fileSystem.url(filename)

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    add = News(name=newstitle,
                               short_txt=newstxtshort,
                               body_txt=newstxt,
                               date="2020",
                               pic_name=filename,
                               pic_url=url,
                               writer="-",
                               category_name="-",
                               category_id=0,
                               show=0, )
                    add.save()
                    return redirect('news_list')
                else:
                    error = "Votre image ne doit pas dépasser 5 MB"
                    return render(request, 'back/error.html', {'error': error})

            else:
                error = "Le format de votre fichier n'est pas supporté"
                return render(request, 'back/error.html', {'error': error})

        except:

            error = "Vous devez téléverser une image"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html')
