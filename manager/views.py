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
from django.contrib.contenttypes.models import ContentType
from news.models import News
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout


def manager_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    manager = Manager.objects.all()

    return render(request, 'back/manager_list.html', {'manager': manager})


def manager_delete(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    manager = Manager.objects.get(pk=pk)

    b = User.objects.filter(username=manager.user_txt)
    b.delete()

    manager.delete()

    messages.success(request, "L'utilisateur a bien été supprimé avec succès")
    return redirect('manager_list')


def manager_group(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès intedit")
        return redirect('panel')

    group = Group.objects.all().exclude(name="masteruser")

    return render(request, 'back/manager_group.html', {'group': group})


def manager_group_add(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    if request.method == 'POST':
        name = request.POST.get('name')

        if name != "":

            if len(Group.objects.filter(name=name)) == 0:
                group = Group(name=name)
                group.save()

    messages.success(request, "Le groupe a bien été ajouté avec succès")
    return redirect(manager_group)


def manager_group_delete(request, name):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    b = Group.objects.filter(name=name)
    b.delete()

    messages.success(request, "Le groupe a bien été supprimé avec succès")
    return redirect(manager_group)


def users_groups(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès intedit")
        return redirect('panel')

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.user_txt)

    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)

    group = Group.objects.all()

    return render(request, 'back/users_groups.html', {'ugroup': ugroup, 'group': group, 'pk': pk})


def add_users_to_groups(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    if request.method == 'POST':
        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.user_txt)
        user.groups.add(group)

    messages.success(request, "Le groupe a bien été ajouté à l'utilisateur")
    return redirect('users_groups', pk=pk)


def del_users_to_groups(request, pk, name):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.user_txt)
    user.groups.remove(group)

    messages.success(request, "Le groupe a bien été supprimé avec succès")
    return redirect('users_groups', pk=pk)


def manager_perms(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    perms = Permission.objects.all()

    return render(request, 'back/manager_perms.html', {'perms': perms})


def manager_perms_del(request, name):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    perms = Permission.objects.filter(name=name)
    perms.delete()

    messages.success(request, "La permission a bien été supprimé avec succès")
    return redirect('manager_perms')


def manager_perms_add(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    if request.method == 'POST':

        name = request.POST.get('name')
        cname = request.POST.get('cname')

        if len(Permission.objects.filter(codename=cname)) == 0:

            content_type = ContentType.objects.get(app_label='main', model='main')
            permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)

        else:
            messages.error(request, "Le code name existe déjà")
            return redirect('manager_perms')

    messages.success(request, "La permission a bien été ajouté avec succès")
    return redirect('manager_perms')


def users_perms(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.user_txt)

    permission = Permission.objects.filter(user=user)

    uperms = []
    for i in permission:
        uperms.append(i.name)

    perms = Permission.objects.all()

    return render(request, 'back/users_perms.html', {'uperms': uperms, 'pk': pk, 'perms': perms})


def users_perms_del(request, pk, name):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.user_txt)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)

    messages.success(request, "La permission de l'utilisateur a bien été supprimé avec succès")
    return redirect('users_perms', pk=pk)


def users_perms_add(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        messages.error(request, "Acccès interdit")
        return redirect('panel')

    if request.method == 'POST':

        pname = request.POST.get('pname')

        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.user_txt)

        permission = Permission.objects.get(name=pname)
        user.user_permissions.add(permission)

    messages.success(request, "La permission a bien été ajouté avec succès")
    return redirect('users_perms', pk=pk)

