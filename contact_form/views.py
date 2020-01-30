from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactForm
from category.models import Category
from main.models import Main
from news.models import News
from subcategory.models import SubCategory


def contact_add(request):

    site = Main.objects.get(pk=3)
    allNews = News.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popularynews = News.objects.all().order_by('-show')[:4]
    popularynews_footer = News.objects.all().order_by('-show')[:4]

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

        b = ContactForm(name=name, email=email, msg=msg)
        b.save()

        messages.success(request, 'Votre message a été transmit avec succée')
        return redirect('home')

    context = {
        'site': site,
        'category': category,
        'subcat': subcat,
        'allNews': allNews,
        'popularynews_footer': popularynews_footer,
        'lastnews': lastnews,
        'popularynews': popularynews

    }

    return render(request, 'front/contact.html', context)
