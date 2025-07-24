from django.db import models

# Create your models here.
class Actor(models.Model):
    @property
    def movies(self):
        return Movie.objects.filter(roles__actor=self)

class Movie(models.Model):
    @property
    def actors(self):
        return Actor.objects.filter(roles__movie=self)

class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')

