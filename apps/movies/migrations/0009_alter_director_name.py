# Generated by Django 5.0.6 on 2024-07-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0008_alter_genre_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="director",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]