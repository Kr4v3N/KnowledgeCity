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
    writer.writerow(['Identifiant', 'Nom de la catégorie', "Nombre d'articles"])
    for i in Category.objects.all():
        writer.writerow([i.id, i.name, i.count])
    return response


def import_cat_csv(request):
    if request.method == 'POST':

        csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Mauvais format')
            return redirect(category_list)

        if csv_file.multiple_chunks():
            messages.error(request, 'Le fichier est trop volumineux')
            return redirect(category_list)

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")

        for line in lines:

            fields = line.split(",")

            try:
                if len(Category.objects.filter(Identifiant=fields[0])) == 0 and fields[0] != "Nom de la catégorie" \
                        and fields[0] != "":
                    b = Category(name=fields[0])
                    b.save()
            except:
                print('finish')

    return redirect('category_list')
