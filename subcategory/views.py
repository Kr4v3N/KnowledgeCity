from django.contrib import messages
from django.shortcuts import render, redirect
from .models import SubCategory
from category.models import Category


def subcategory_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    subcat = SubCategory.objects.all()

    return render(request, 'back/subcategory_list.html', {'subcategory': subcat})


def subcategory_add(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    cat = Category.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name')
        catid = request.POST.get('category')

        if name == "":
            messages.warning(request, "Vous devez ajouter une sous-catégorie")
            return redirect('subcategory_add')

        if len(SubCategory.objects.filter(name=name)) != 0:
            messages.warning(request, "Cette sous-catégorie existe déjà")
            return redirect('subcategory_add')

        catname = Category.objects.get(pk=catid).name

        b = SubCategory(name=name, category_name=catname, category_id=catid)
        b.save()
        messages.success(request, "La sous catégorie a bien été ajoutée")
        return redirect('subcategory_list')

    return render(request, 'back/subcategory_add.html', {'category': cat})
