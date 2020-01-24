from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcategory.models import SubCategory

# Create your views here.


def news_detail(request, pk):
    site = Main.objects.get(pk=3)
    news = News.objects.filter(pk=pk)

    return render(request, 'front/news_detail.html', {'news': news, 'site': site})


def news_list(request):
    news = News.objects.all()

    return render(request, 'back/news_list.html', {'news': news})


def news_add(request):
    now = datetime.datetime.now()

    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    if len(str(month)) == 1:
        month = '0' + str(month)
    if len(str(day)) == 1:
        day = '0' + str(day)
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(minute)) == 1:
        minute = '0' + str(minute)

    today = str(day) + '/' + str(month) + '/' + str(year)
    time = str(hour) + '/' + str(minute)

    cat = SubCategory.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscategory')

        if newstitle == "" or newstxt == "" \
                or newstxtshort == "" \
                or newscategory == "" \
                or newstitle == "":
            error = "Tous les champs sont requis"
            return render(request, 'back/error.html', {'error': error})

        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    newsname = SubCategory.objects.get(pk=newsid).name

                    add = News(name=newstitle,
                               short_txt=newstxtshort,
                               body_txt=newstxt,
                               date=today,
                               pic_name=filename,
                               pic_url=url,
                               writer="-",
                               category_name=newsname,
                               category_id=newsid,
                               show=0,
                               time=time, )
                    add.save()
                    return redirect('news_list')

                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "L'image ne doit pas dépasser 5 MB"
                    return render(request, 'back/error.html', {'error': error})

            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Le format de votre fichier n'est pas supporté"
                return render(request, 'back/error.html', {'error': error})

        except:

            error = "Vous devez téléverser une image"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html', {'category': cat})


def news_delete(request, pk):
    try:

        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.pic_name)
        b.delete()

    except:

        error = "Quelque chose c'est mal passée"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')
