from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    review = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self) ->str:
        return f"In {self.review_date}, the user {self.user} made a review for the movie: {self.movie}"

    class Meta:
        verbose_name_plural ='Reviews'
