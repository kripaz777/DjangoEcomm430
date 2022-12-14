# Generated by Django 4.1.1 on 2022-10-13 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=300)),
                ("email", models.EmailField(max_length=100)),
                ("subject", models.TextField()),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
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
                ("username", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300)),
                (
                    "items",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.product"
                    ),
                ),
            ],
        ),
    ]
