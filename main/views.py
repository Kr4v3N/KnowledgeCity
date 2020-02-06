import random
import string

from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib import messages
from random import randint
from category.models import Category
from manager.models import Manager
from trending.models import Trending
from .models import Main
from news.models import News
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout


def home(request):
    site = Main.objects.get(pk=3)
    news = News.objects.filter(activated=1).order_by('-pk')
    allNews = News.objects.filter(activated=1)
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    lastnews = News.objects.filter(activated=1).order_by('-pk')[:4]
    popularynews = News.objects.filter(activated=1).order_by('-show')
    popularynews1 = News.objects.filter(activated=1).order_by('-show')[:1]
    popularynews_footer = News.objects.filter(activated=1).order_by('-show')[:4]
    trending = Trending.objects.all().order_by('-pk')[:5]

    # random_object = Trending.objects.all()[randint(0, len(trending) - 1)]
    # print(random_object)

    return render(request, 'home.html', {'site': site,
                                         'news': news,
                                         'allNews': allNews,
                                         'category': category,
                                         'subcat': subcat,
                                         'lastnews': lastnews,
                                         'popularynews': popularynews,
                                         'popularynews1': popularynews1,
                                         'popularynews_footer': popularynews_footer,
                                         'trending': trending
                                         })


def about(request):
    site = Main.objects.get(pk=3)
    allNews = News.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popularynews = News.objects.all().order_by('-show')[:4]
    popularynews_footer = News.objects.all().order_by('-show')[:4]
    trending = Trending.objects.all().order_by('-pk')[:5]

    return render(request, 'front/about.html', {'site': site,
                                                'category': category,
                                                'subcat': subcat,
                                                'allNews': allNews,
                                                'popularynews_footer': popularynews_footer,
                                                'lastnews': lastnews,
                                                'popularynews': popularynews,
                                                'trending': trending
                                                })


def panel(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms:
        if i.codename == "master_user": perm = 1
    # print(i.codename)
    # if perm == 0:
    #     messages.error(request, "Accès interdit")
    # return redirect('change_pass')
    '''
    rand = ""
    specialchars = ['!', '@', '$', '%', '&', '^', ')', '=', '(', '-', ')', 'ç', '/', 'µ', '*', '#']
    for i in range(20):
        rand = rand + random.choice(string.ascii_letters)
        rand += random.choice(specialchars)
        rand += str(random.randint(8, 10))
    '''

    count = News.objects.count()
    rand = News.objects.all()[random.randint(0, count-1)]

    return render(request, 'back/admin_home.html', {'rand': rand})


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


def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_verify = request.POST.get('password-verify')
        # print(username, password, password_verify)

        if name == "":
            messages.error(request, "Vous devez saisir un nom")
            return redirect('register')

        if uname == "":
            messages.error(request, "Vous devez saisir un nom d'utilisateur")
            return redirect('register')

        if len(name) < 2:
            messages.error(request, "Votre nom doit comporter au moins 2 caractères")
            return redirect('register')

        if len(uname) < 2:
            messages.error(request, "Votre nom d'utilisateur doit comporter au moins 2 caractères")
            return redirect('register')

        try:
            validate_email(request.POST.get("email"))
        except ValidationError:
            messages.error(request, 'Entrez une adresse mail valide')
            return redirect('register')

        if password != password_verify:
            messages.error(request, "Les mots de passe saisis ne sont pas identiques")
            return redirect('register')

        count4 = 0
        count5 = 0
        count6 = 0

        for i in password:
            if '0' < i < '9':
                count4 += 1
            if 'A' < i < 'Z':
                count5 += 1
            if 'a' < i < 'z':
                count6 += 1

        if count4 == 0 or count5 == 0 or count6 == 0:
            messages.error(request,
                           "Votre mot de passe doit comporter au moins 8 caractères avec des chiffres, des lettres "
                           "minuscules et majuscules")
            return redirect('register')

        if len(password) < 8:
            messages.error(request, "Votre mot de passe doit comporter plus de 8 caractères")
            return redirect('register')

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:
            user = User.objects.create_user(username=uname, email=email, password=password)
            b = Manager(name=name, user_txt=uname, email=email)
            b.save()

    return render(request, 'front/login.html')


def user_logout(request):
    logout(request)

    return redirect('login')


def site_settings(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

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
            messages.error(request, "Tous les champs doivent être renseignés")
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


def about_settings(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    if request.method == 'POST':
        txt = request.POST.get('txt')
        if txt == "":
            messages.error(request, "Tous les champs doivent être renseignés")
            return redirect('about_settings')

        b = Main.objects.get(pk=3)
        b.about_page = txt
        b.save()
        messages.success(request, "Votre page à bien été modifié")
        return redirect('about_settings')

    about_page = Main.objects.get(pk=3).about_page

    context = {
        'about_page': about_page
    }

    return render(request, 'back/about_setting.html', context)


def contact(request):
    site = Main.objects.get(pk=3)
    allNews = News.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popularynews = News.objects.all().order_by('-show')[:4]
    popularynews_footer = News.objects.all().order_by('-show')[:4]
    trending = Trending.objects.all().order_by('-pk')[:5]

    context = {
        'site': site,
        'allNews': allNews,
        'category': category,
        'lastnews': lastnews,
        'subcat': subcat,
        'popularynews': popularynews,
        'popularynews_footer': popularynews_footer,
        'trending': trending
    }

    return render(request, 'front/contact.html', context)


def change_pass(request, user=None):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    if request.method == 'POST':
        old_pass = request.POST.get('old_pass')
        new_pass = request.POST.get('new_pass')
        new_pass_confirm = request.POST.get('new_pass_confirm')

        if old_pass == "" or new_pass == "" or new_pass_confirm == "":
            messages.error(request, 'Tous les champs sont requis')
            return redirect('change_pass')

        user = authenticate(username=request.user, password=old_pass)

        if user is not None:

            if new_pass != new_pass_confirm:
                messages.error(request,
                               "Le champ nouveau mot de passe doit être identique au champ confirmer nouveau mot de "
                               "passe")
                return redirect('change_pass')

            if len(new_pass) < 8:
                messages.error(request, "Votre mot de passe doit comporter plus de 8 caractères")
                return redirect('change_pass')

            count1 = 0
            count2 = 0
            count3 = 0

            for i in new_pass:
                if '0' < i < '9':
                    count1 += 1
                if 'A' < i < 'Z':
                    count2 += 1
                if 'a' < i < 'z':
                    count3 += 1
            # print(count1, count2, count3)

            if count1 >= 1 and count2 >= 1 and count3 >= 1:
                user = User.objects.get(username=request.user)
                user.set_password(new_pass)
                user.save()
                messages.success(request, 'Votre mot de passe a été modifié avec succès')
                return redirect('panel')
            else:
                messages.error(request, "Votre mot de passe doit comporter au moins 8 caractères avec des chiffres, "
                                        "des lettres minuscules et majuscules")
                return redirect('logout')

        else:
            messages.error(request, "Votre ancien mot de passe n'est pas valide")
            return redirect('change_pass')

    return render(request, 'back/change_pass.html')
