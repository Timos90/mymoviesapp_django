# Generated by Django 5.0.6 on 2024-07-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("deleted_movies", "0003_alter_deletedmovies_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="deletedmovies",
            options={"verbose_name_plural": "Deleted movies"},
        ),
    ]
