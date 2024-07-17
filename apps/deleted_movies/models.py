from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DeletedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.OneToOneField('movies.Movie', on_delete=models.CASCADE)

    def __str__(self) ->str:
        return f"The movie {self.movie} is deleted from the user ({self.user})"

    class Meta:
        verbose_name_plural = 'Deleted movies'
        unique_together = ('user', 'movie')
