from django.db import models

class Album(models.Model):
    album_name = models.CharField(max_length=250)
    album_artist = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField(max_length=1000)
    format = models.CharField(max_length=100)


    def __str__(self):
        return self.album_name + " - " + self.album_artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=250)
    song_time = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.song_name

class Single(models.Model):
    single_name = models.CharField(max_length=250)
    single_artist = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField(max_length=1000)


    def __str__(self):
        return self.single_name + " - " + self.single_artist




