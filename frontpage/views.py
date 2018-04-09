from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/frontpage/' + str(album.id) + '/'
        html += '<a href="' + url + '">' +  album.album_name + '</a> <br>'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Details for album: " + album_id + "</h2>")