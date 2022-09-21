# Generated by Django 4.1.1 on 2022-09-20 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=400)),
                ("price", models.IntegerField()),
                ("discounted_price", models.IntegerField()),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                (
                    "stock",
                    models.CharField(
                        choices=[
                            ("In stock", "In stock"),
                            ("out of stock", "out of stock"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "labels",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("new", "new"),
                            ("hot", "hot"),
                            ("sale", "sale"),
                            ("", "default"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.brand"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.category"
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.subcategory",
                    ),
                ),
            ],
        ),
    ]