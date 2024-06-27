from django.db import models
from apps.users.models import Users
from apps.movies.models import Movies
from django.contrib.postgres.validators import (
    RangeMaxValueValidator,
    RangeMinValueValidator
)

# Create your models here.
class Ratings(models.Model):
    rating_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[RangeMinValueValidator(1.0), RangeMaxValueValidator(10.1)])
    rating_date = models.DateField(auto_now_add=True)
