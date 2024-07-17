# Generated by Django 5.0.6 on 2024-07-11 21:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("deleted_movies", "0005_rename_deletedmovies_deletedmovie"),
        ("movies", "0014_alter_movie_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="deletedmovie",
            unique_together={("user", "movie")},
        ),
    ]