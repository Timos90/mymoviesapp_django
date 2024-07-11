from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField()
    rating_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Ratings'
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1.0) & models.Q(rating__lte=10.0),
                name='rating_range'
            ),
        ]

    def __str__(self) ->str:
        return f"In {self.rating_date}, the user {self.user} rated the movie'{self.movie}' with ({self.rating})"
