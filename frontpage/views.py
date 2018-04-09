from django.http import Http404

from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'frontpage/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Sorry! This album is not for sale right now. Please check back later")
    return render(request, 'frontpage/detail.html', {'album': album})
