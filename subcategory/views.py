from django.shortcuts import render, redirect
from .models import SubCategory
from category.models import Category


# Create your views here.

def subcategory_list(request):

    subcat = SubCategory.objects.all()

    return render(request, 'back/subcategory_list.html', {'subcategory': subcat})


def subcategory_add(request):

    cat = Category.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name')
        catid = request.POST.get('category')

        if name == "":
            error = "Vous devez ajouter une sous-catégorie"
            return render(request, 'back/error_subcategory.html', {'error': error})

        if len(SubCategory.objects.filter(name=name)) != 0:

            error = "Cette sous-catégorie existe déjà"
            return render(request, 'back/error_subcategory.html', {'error': error})

        catname = Category.objects.get(pk=catid).name

        b = SubCategory(name=name, category_name=catname, category_id=catid)
        b.save()
        return redirect('subcategory_list')

    return render(request, 'back/subcategory_add.html', {'category': cat})
