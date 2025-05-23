# Generated by Django 5.0.6 on 2024-07-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FaceRecord",
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
                ("image", models.ImageField(upload_to="faces/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(default="Unknown", max_length=255)),
            ],
        ),
    ]
