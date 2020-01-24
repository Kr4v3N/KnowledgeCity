from django.shortcuts import render, redirect
from .models import SubCategory


# Create your views here.

def subcategory_list(request):
    subcat = SubCategory.objects.all()
    return render(request, 'back/subcategory_list.html', {'subcategory': subcat})


def subcategory_add(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        if name == "":
            error = "Vous devez ajouter une catégorie"
            return render(request, 'back/error_category.html', {'error': error})

        if len(SubCategory.objects.filter(name=name)) != 0:

            error = "Cette catégorie existe déjà"
            return render(request, 'back/error_category.html', {'error': error})

        else:

            b = SubCategory(name=name)
            b.save()
            return redirect('subcategory_list')

    return render(request, 'back/subcategory_add.html')
