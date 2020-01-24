from django.shortcuts import render, redirect
from .models import Category


# Create your views here.

def category_list(request):

    cat = Category.objects.all()
    return render(request, 'back/category_list.html', {'category': cat})


def category_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')

        if name == "":
            error = "Vous devez ajouter une catégorie"
            return render(request, 'back/error_category.html', {'error': error})

        if len(Category.objects.filter(name=name)) != 0:

            error = "Cette catégorie existe déjà"
            return render(request, 'back/error_category.html', {'error': error})

        else:
            
            b = Category(name=name)
            b.save()
            return redirect('category_list')

    return render(request, 'back/category_add.html')
