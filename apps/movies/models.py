from django.db import models
from apps.users.models import Users

# Create your models here.
class Movies(models.Model):
    movieid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    releaseyear = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
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
    added_by_user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)