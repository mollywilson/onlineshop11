from django.contrib import admin
from .models import Album, Single, Song

admin.site.register(Album)
admin.site.register(Single)
admin.site.register(Song)