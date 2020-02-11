from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from comment.models import Comment
from manager.models import Manager
from news.models import News


def comment_add(request, pk):

    if request.method == 'POST':
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

        content = request.POST.get('msg')

        if request.user.is_authenticated:

            manager = Manager.objects.get()

            b = Comment(name=manager.name,
                        email=manager.email,
                        content=content,
                        news_id=pk,
                        date=today,
                        time=time
                        )
            b.save()
        else:

            newsname1 = News.objects.get(pk=pk).name

            name = request.POST.get('name')
            email = request.POST.get('email')

            if name == "":
                messages.error(request, "Vous devez saisir un nom d'utilisateur")
                return redirect('news_detail', word=newsname1)

            if len(name) < 3:
                messages.error(request, "Le nom doit comporter au moins 3 caractères")
                return redirect('news_detail', word=newsname1)

            if email == "":
                messages.error(request, "Vous devez saisir une adresse mail")
                return redirect('news_detail', word=newsname1)

            try:
                validate_email(request.POST.get("email"))
            except ValidationError:
                messages.error(request, 'Entrez une adresse mail valide')
                return redirect('news_detail', word=newsname1)

            if content == "":
                messages.error(request, "Vous devez saisir un commentaire")
                return redirect('news_detail', word=newsname1)

            if len(content) < 10:
                messages.error(request, "Le commentaire doit comporter au moins 10 caractères")
                return redirect('news_detail', word=newsname1)

            b = Comment(name=name,
                        email=email,
                        content=content,
                        news_id=pk,
                        date=today,
                        time=time
                        )
            b.save()

    newsname = News.objects.get(pk=pk).name

    messages.success(request, "Votre commentaire a été soumis avec succès")
    return redirect('news_detail', word=newsname)


def comment_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).writer
        # print(a, request.user)
        if str(a) != str(request.user):
            messages.error(request, "Accès refusé")
            return redirect('news_list')

    comments = Comment.objects.all()

    return render(request, 'back/comments_list.html', {'comments': comments})


def comment_delete(request, pk):
    comment = Comment.objects.filter(pk=pk)
    comment.delete()

    messages.success(request, 'Le commentaire a été supprimé avec succès')
    return redirect('comments_list')


def comment_confirm(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # Login check end

    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()

    return redirect('comments_list')
