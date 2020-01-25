from django.contrib import messages
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
