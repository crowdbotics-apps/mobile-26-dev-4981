# Generated by Django 2.2.12 on 2020-05-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="Abcd",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gfgf", models.BigIntegerField()),
            ],
        ),
    ]
