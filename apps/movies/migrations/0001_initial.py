# Generated by Django 5.0.6 on 2024-06-27 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movies",
            fields=[
                ("movieid", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("releaseyear", models.IntegerField(blank=True, null=True)),
                ("genre", models.CharField(blank=True, max_length=255, null=True)),
                ("director", models.CharField(blank=True, max_length=255, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
                ("runtime", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("language", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("boxoffice", models.BigIntegerField(blank=True, null=True)),
                ("awards", models.TextField(blank=True, null=True)),
                ("casting", models.TextField(blank=True, null=True)),
                (
                    "productioncompany",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("budget", models.BigIntegerField(blank=True, null=True)),
                ("releasedate", models.DateField(blank=True, null=True)),
                ("productioncompanyid", models.IntegerField(blank=True, null=True)),
                ("deleted", models.BooleanField(default=False)),
                (
                    "added_by_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.users",
                    ),
                ),
            ],
        ),
    ]