from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactForm
from category.models import Category
from main.models import Main
from news.models import News
from subcategory.models import SubCategory


def contact_add(request):
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
    time = str(hour) + 'H' + str(minute)

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        if name == "" or email == "" or msg == "":
            messages.error(request, 'Tous les champs sont requis')
            return redirect('contact_add')

        try:
            validate_email(request.POST.get("email"))
        except ValidationError:
            messages.error(request, 'Entrez une adresse mail valide')
            return redirect('contact_add')

        b = ContactForm(name=name, email=email, msg=msg, date=today, time=time)
        b.save()

        messages.success(request, 'Votre message a été envoyée avec succès')
        return redirect('home')

    site = Main.objects.get(pk=3)
    allNews = News.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popularynews = News.objects.all().order_by('-show')[:4]
    popularynews_footer = News.objects.all().order_by('-show')[:4]

    context = {
        'site': site,
        'category': category,
        'subcat': subcat,
        'allNews': allNews,
        'popularynews_footer': popularynews_footer,
        'lastnews': lastnews,
        'popularynews': popularynews,
    }

    return render(request, 'front/contact.html', context)


def contact_show(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    msg = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'msg': msg})


def contact_delete(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    b = ContactForm.objects.filter(pk=pk)
    b.delete()
    messages.success(request, ' Le message a été supprimé avec succès')

    return redirect('contact_show')


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
                               "Le champ nouveau mot de passe doit être identique au champ confirmer nouveau mot de passe")
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
            print(count1, count2, count3)

            if count1 >= 1 and count2 >= 1 and count3 >= 1:
                user = User.objects.get(username=request.user)
                user.set_password(new_pass)
                user.save()
                messages.success(request, 'Votre mot de passe a été modifié avec succès')
                return redirect('panel')
            else:
                messages.error(request, "Votre mot de passe doit comporter au moins 1 chiffre, 1 lettre minuscule et majuscule")
                return redirect('logout')

        else:
            messages.error(request, "Votre ancien mot de passe n'est pas valide")
            return redirect('change_pass')

    return render(request, 'back/change_pass.html')
