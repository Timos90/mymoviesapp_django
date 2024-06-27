from django.db import models
from apps.users.models import Users
from apps.movies.models import Movies

# Create your models here.
class DeletedMovies(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movies, on_delete=models.CASCADE)
