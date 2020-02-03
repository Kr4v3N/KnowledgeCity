from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib import messages
from random import randint
from category.models import Category
from trending.models import Trending
from .models import Manager
from news.models import News
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout


def manager_list(request):
    manager = Manager.objects.all()

    return render(request, 'back/manager_list.html', {'manager': manager})


def manager_delete(request, pk):
    manager = Manager.objects.get(pk=pk)

    b = User.objects.filter(username=manager.user_txt)
    b.delete()

    manager.delete()

    messages.success(request, "L'utilisateur a bien été supprimé avec succès")
    return redirect('manager_list')


def manager_group(request):
    group = Group.objects.all()

    return render(request, 'back/manager_group.html', {'group': group})


def manager_group_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name != "":

            if len(Group.objects.filter(name=name)) == 0:
                group = Group(name=name)
                group.save()

    messages.success(request, "Le groupe a bien été ajouté avec succès")
    return redirect(manager_group)


def manager_group_delete(request, name):
    b = Group.objects.filter(name=name)
    b.delete()

    messages.success(request, "Le groupe a bien été supprimé avec succès")
    return redirect(manager_group)


def users_groups(request, pk):
    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.user_txt)

    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)

    group = Group.objects.all()

    return render(request, 'back/users_groups.html', {'ugroup': ugroup, 'group': group, 'pk': pk})


def add_users_to_groups(request, pk):

    if request.method == 'POST':

        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.user_txt)
        user.groups.add(group)

    messages.success(request, "Le groupe a bien été ajouté à l'utilisateur")
    return redirect('users_groups', pk=pk)
