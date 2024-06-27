from django.db import models
from apps.users.models import Users
from apps.movies.models import Movies

# Create your models here.
class UserMovies(models.Model):
    user_movie_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
