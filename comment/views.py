import random
import string
from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.core.validators import validate_email
from django.shortcuts import render, redirect

from news.models import News


def comment_add(request, pk):

    newsname = News.objects.get(pk=pk)

    return redirect('news_detail', word=newsname)
