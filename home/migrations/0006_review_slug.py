# Generated by Django 4.1.1 on 2022-10-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="slug",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]