from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib import messages
from random import randint
import datetime
from django.utils import timezone
from django.db.models.functions import datetime
from category.models import Category
from trending.models import Trending
from .models import Newsletter
from django.contrib.contenttypes.models import ContentType
from news.models import News
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout


def news_letter(request):
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
        txt = request.POST.get('register-email')

        b = Newsletter(txt=txt,
                       status=1,
                       date=today,
                       time=time,
                       )
        b.save()

    messages.success(request, "Merci pour votre inscription")
    return redirect('home')


def news_emails(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    emails = Newsletter.objects.filter(status=1)

    return render(request, 'back/emails.html', {'emails': emails})
