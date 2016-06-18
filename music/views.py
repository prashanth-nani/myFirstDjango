# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, "music/index.html", context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
        context = {'album': album}
    except Album.DoesNotExist:
        raise Http404("The album does not exist")
    return render(request, "music/detail.html", context)
