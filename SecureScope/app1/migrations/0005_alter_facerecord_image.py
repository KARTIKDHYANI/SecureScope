# Generated by Django 5.0.6 on 2024-07-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0004_alter_facerecord_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facerecord",
            name="image",
            field=models.ImageField(upload_to="person_records/faces/"),
        ),
    ]
