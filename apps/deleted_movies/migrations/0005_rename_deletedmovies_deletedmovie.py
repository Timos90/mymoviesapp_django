# Generated by Django 5.0.6 on 2024-07-10 22:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("deleted_movies", "0004_alter_deletedmovies_options"),
        ("movies", "0006_alter_movies_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DeletedMovies",
            new_name="DeletedMovie",
        ),
    ]
