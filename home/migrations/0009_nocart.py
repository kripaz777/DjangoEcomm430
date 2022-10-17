# Generated by Django 4.1.1 on 2022-10-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_contact_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="NoCart",
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
                ("user", models.CharField(max_length=200)),
                ("count", models.IntegerField()),
            ],
        ),
    ]
