# Generated by Django 5.0.6 on 2024-07-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0012_alter_movie_boxoffice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="budget",
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
