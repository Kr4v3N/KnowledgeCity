from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from category.models import Category
from .models import Main
from news.models import News
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout


def home(request):

    site = Main.objects.get(pk=3)
    news = News.objects.all().order_by('-pk')
    allNews = News.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popularynews = News.objects.all().order_by('-show')

    return render(request, 'home.html', {'site': site,
                                         'news': news,
                                         'allNews': allNews,
                                         'category': category,
                                         'subcat': subcat,
                                         'lastnews': lastnews,
                                         'popularynews': popularynews

                                         })


def about(request):

    site = Main.objects.get(pk=3)
    allNews = News.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()

    return render(request, 'front/about.html', {'site': site,
                                                'category': category,
                                                'subcat': subcat,
                                                'allNews': allNews,
                                                })


def panel(request):

    # TODO Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # TODO Login chek end

    return render(request, 'back/admin_home.html')


def user_login(request):

    if request.method == 'POST':
        user_txt = request.POST.get('username')
        pass_txt = request.POST.get('password')

        if user_txt != "" and pass_txt != "":
            user = authenticate(username=user_txt, password=pass_txt)

            if user is not None:
                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def user_logout(request):

    logout(request)

    return redirect('login')


def site_settings(request):

    # TODO Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # TODO Login chek end

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        facebook = request.POST.get('facebook')
        linkedin = request.POST.get('linkedin')
        twitter = request.POST.get('twitter')
        youtube = request.POST.get('youtube')
        link = request.POST.get('link')
        about = request.POST.get('about')

        if facebook == "": facebook == "#"
        if twitter == "": twitter == "#"
        if linkedin == "": linkedin == "#"
        if youtube == "": youtube == "#"
        if link == "": link == "#"

        if name == "" or phone == "" or about == "":
            messages.warning(request, "Tous les champs doivent être renseignés")
            return redirect('site_settings')
        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            pic_url = url
            pic_name = filename

        except:

            pic_url = "-"
            pic_name = "-"

        try:

            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            pic_url_footer = url2
            pic_name_footer = filename2

        except:

            pic_url_footer = "-"
            pic_name_footer = "-"

        b = Main.objects.get(pk=3)

        b.name = name
        b.phone = phone
        b.facebook = facebook
        b.twitter = twitter
        b.linkedin = linkedin
        b.youtube = youtube
        b.link = link
        if pic_url != "-": b.pic_url = pic_url
        if pic_name != "-": b.pic_name = pic_name
        if pic_url_footer != "-": b.pic_url_footer = pic_url_footer
        if pic_name_footer != "-": b.pic_name_footer = pic_name_footer
        b.save()

    site = Main.objects.get(pk=3)

    return render(request, 'back/settings.html', {'site': site})
