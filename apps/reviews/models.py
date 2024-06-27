from django.db import models
from apps.users.models import Users
from apps.movies.models import Movies

# Create your models here.
class Reviews(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    review = models.TextField()
    review_date = models.DateField(auto_now_add=True)
