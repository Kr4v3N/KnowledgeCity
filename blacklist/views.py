from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv

from .models import Blacklist


def black_list(request):
    ip = Blacklist.objects.all()

    return render(request, 'back/blacklist.html', {'ip': ip})


def ip_add(request):
    if request.method == 'POST':

        ip = request.POST.get('ip')

        if ip != "":
            b = Blacklist(ip=ip)
            b.save()

    return redirect(black_list)


def ip_delete(request, pk):
    b = Blacklist.objects.filter(pk=pk)
    b.delete()

    messages.success(request, "L'IP a été supprimé avec succès")
    return redirect(black_list)



