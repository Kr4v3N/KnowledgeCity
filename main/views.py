from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


# Create your views here.

def home(request):

    site = Main.objects.get(pk=3)

    return render(request, 'home.html', {'site': site})


def about(request):

    site = Main.objects.get(pk=3)

    return render(request, 'front/about.html', {'site': site})
