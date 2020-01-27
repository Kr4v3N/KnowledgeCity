from django.shortcuts import render, get_object_or_404, redirect

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

    return render(request, 'home.html', {'site': site,
                                         'news': news,
                                         'allNews': allNews,
                                         'category': category,
                                         'subcat': subcat,
                                         'lastnews': lastnews
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

    site = Main.objects.get(pk=3)

    context = {
        'site': site
    }

    return render(request, 'back/settings.html', context)
