# Generated by Django 5.0.6 on 2024-07-11 11:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0007_rename_movies_movie"),
        ("user_movies", "0003_alter_usermovies_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UserMovies",
            new_name="UserMovie",
        ),
    ]
