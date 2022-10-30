from django.db import models

# Create your models here.

# Attributes for “Song” : title, date released, likes, artiste_id
# Attributes for “Lyric”: content, song_id

class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
