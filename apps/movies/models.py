from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MoviesManager(models.Manager):
    # self = <Model>.objects
    def get_movies_by_tags(self, *tags):
        return self.filter(tags__name__in=tags)

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    movieid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    releaseyear = models.IntegerField(null=True, blank=True)
    # genre = models.CharField(max_length=255, null=True, blank=True)
    # director = models.CharField(max_length=255, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    boxoffice = models.BigIntegerField(null=True, blank=True)
    awards = models.TextField(null=True, blank=True)
    casting = models.TextField(null=True, blank=True)
    productioncompany = models.CharField(max_length=255, null=True, blank=True)
    budget = models.BigIntegerField(null=True, blank=True)
    releasedate = models.DateField(null=True, blank=True)
    productioncompanyid = models.IntegerField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    added_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='directed_movies')
    tags = models.ManyToManyField(Tag, related_name='tagged_movies')

    objects = MoviesManager

    def __str__(self) ->str:
        return f"{self.title}({self.releaseyear})"

    class Meta:
        verbose_name_plural = 'Movies'
    