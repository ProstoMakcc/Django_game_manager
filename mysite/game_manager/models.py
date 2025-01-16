from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name

class Game(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    pub_date = models.DateField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name

