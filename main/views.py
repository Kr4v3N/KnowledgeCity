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
        usertxt = request.POST.get('username')
        passtxt = request.POST.get('password')

        if usertxt != "" and passtxt != "":
            user = authenticate(username=usertxt, password=passtxt)

            if user is not None:
                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')
