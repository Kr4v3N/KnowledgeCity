import csv

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category


# Create your views here.

def category_list(request):

    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    cat = Category.objects.all()

    return render(request, 'back/category_list.html', {'category': cat})


def category_add(request):

    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    if request.method == 'POST':
        name = request.POST.get('name')

        if name == "":
            messages.warning(request, "Vous devez ajouter une catégorie")
            return redirect('category_add')

        if len(Category.objects.filter(name=name)) != 0:

            messages.warning(request, "Cette catégorie existe déjà")
            return redirect('category_add')

        else:
            
            b = Category(name=name)
            b.save()
            messages.success(request, "La catégorie a bien été ajoutée")
            return redirect('category_list')

    return render(request, 'back/category_add.html')


def export_cat_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="category.csv'

    writer = csv.writer(response)
    writer.writerow(['test1', 'test2', 'test3'])

    return response