# Generated by Django 4.1 on 2024-11-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post_test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("text", models.TextField()),
            ],
        ),
    ]
