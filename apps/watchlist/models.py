from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Watchlist(models.Model):
    watchlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) ->str:
        return f"The user {self.user} added the movie'{self.movie}' in his watchlist)"
    