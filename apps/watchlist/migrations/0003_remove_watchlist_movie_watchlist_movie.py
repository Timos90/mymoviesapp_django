# Generated by Django 5.0.6 on 2024-07-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_movies_movieid"),
        ("watchlist", "0002_alter_watchlist_watchlist_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="movie",
        ),
        migrations.AddField(
            model_name="watchlist",
            name="movie",
            field=models.ManyToManyField(to="movies.movies"),
        ),
    ]
