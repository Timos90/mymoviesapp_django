# Generated by Django 5.0.6 on 2024-06-30 17:13

import django.contrib.postgres.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ratings",
            fields=[
                ("rating_id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "rating",
                    models.FloatField(
                        validators=[
                            django.contrib.postgres.validators.RangeMinValueValidator(
                                1.0
                            ),
                            django.contrib.postgres.validators.RangeMaxValueValidator(
                                10.1
                            ),
                        ]
                    ),
                ),
                ("rating_date", models.DateField(auto_now_add=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movies"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
