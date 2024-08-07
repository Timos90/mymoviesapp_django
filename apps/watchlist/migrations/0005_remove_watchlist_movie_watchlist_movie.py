# Generated by Django 5.0.6 on 2024-07-10 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_remove_movies_director_remove_movies_genre_and_more"),
        ("watchlist", "0004_alter_watchlist_movie"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="movie",
        ),
        migrations.AddField(
            model_name="watchlist",
            name="movie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="movies.movies",
            ),
        ),
    ]
