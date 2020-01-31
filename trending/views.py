from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from category.models import Category
from .models import Trending
from news.models import News
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def trending_add(request):

    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    if request.method == 'POST':
        txt = request.POST.get('txt')

        if txt == "":
            messages.error(request, "Tous les champs doivent être renseignés")
            return redirect('trending_add')

        b = Trending(txt=txt)
        b.save()
        messages.success(request, "La tendance a été ajouté avec succès ")
        return redirect('trending_add')

    trending = Trending.objects.all().order_by('-pk')

    return render(request, 'back/trending.html', {'trending': trending})


def trending_delete(request, pk):

    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    b = Trending.objects.filter(pk=pk)
    b.delete()
    messages.success(request, ' La tendance a été supprimé avec succès')

    return redirect('trending_add')


def trending_edit(request, pk):

    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    mytxt = Trending.objects.get(pk=pk).txt

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "":
            messages.error(request, "Tous les champs doivent être renseignés")
            return redirect('trending_edit')

        b = Trending.objects.get(pk=pk)
        b.txt = txt
        b.save()
        messages.success(request, "La tendance a été modifiée avec succès ")
        return redirect('trending_add')

    return render(request, 'back/trending_edit.html', {'mytxt': mytxt, 'pk': pk})
