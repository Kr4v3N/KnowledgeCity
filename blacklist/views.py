import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv

from .models import Blacklist


def black_list(request):
    ip = Blacklist.objects.all()

    return render(request, 'back/blacklist.html', {'ip': ip})


def ip_add(request):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    if len(str(month)) == 1:
        month = '0' + str(month)
    if len(str(day)) == 1:
        day = '0' + str(day)
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(minute)) == 1:
        minute = '0' + str(minute)

    today = str(day) + '/' + str(month) + '/' + str(year)
    time = str(hour) + 'H' + str(minute)

    if request.method == 'POST':

        ip = request.POST.get('ip')

        if ip != "":
            b = Blacklist(ip=ip, date=today, time=time)
            b.save()

    messages.success(request, "L'IP a été ajoutée avec succès")
    return redirect('black_list')


def ip_delete(request, pk):
    b = Blacklist.objects.filter(pk=pk)
    b.delete()

    messages.success(request, "L'IP a été supprimé avec succès")
    return redirect(black_list)



