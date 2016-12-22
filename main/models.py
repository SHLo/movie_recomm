from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=256)
    release = models.DateField(blank=True)
    imdb = models.CharField(max_length=256)
    genre_unknown = models.BooleanField(default=False)
    genre_Action = models.BooleanField(default=False)
    genre_Adventure = models.BooleanField(default=False)
    genre_Animation = models.BooleanField(default=False)
    genre_Children = models.BooleanField(default=False)
    genre_Comedy = models.BooleanField(default=False)
    genre_Crime = models.BooleanField(default=False)
    genre_Documentary = models.BooleanField(default=False)
    genre_Drama = models.BooleanField(default=False)
    genre_Fantasy = models.BooleanField(default=False)
    genre_Film_Noir = models.BooleanField(default=False)
    genre_Horror = models.BooleanField(default=False)
    genre_Musical = models.BooleanField(default=False)
    genre_Mystery = models.BooleanField(default=False)
    genre_Romance = models.BooleanField(default=False)
    genre_Sci_Fi = models.BooleanField(default=False)
    genre_Thriller = models.BooleanField(default=False)
    genre_War = models.BooleanField(default=False)
    genre_Western = models.BooleanField(default=False)


class Rating(models.Model):
    user = models.CharField(max_length=20)
    item = models.ForeignKey(Item)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length=64)


class Genre(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=64)
