# Generated by Django 5.1 on 2024-11-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogmatics", "0004_preprint_abstract"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preprint",
            name="abstract",
            field=models.TextField(null=True),
        ),
    ]