# Generated by Django 5.0.6 on 2024-07-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0010_alter_movie_releaseyear"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="runtime",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]