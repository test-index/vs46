# Generated by Django 4.1.1 on 2023-05-21 16:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("animal_photos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalphotos",
            name="photo",
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
