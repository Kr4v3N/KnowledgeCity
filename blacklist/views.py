from django.shortcuts import render

from .models import Blacklist


def black_list(request):


    return render(request, 'back/blacklist.html')
