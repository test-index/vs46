# Generated by Django 4.1.7 on 2023-04-18 21:08

import django.core.validators
from django.db import migrations, models
import shelter_v11.animal_photos.validators
import shelter_v11.commons.model_mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='animal_photos/', validators=[shelter_v11.animal_photos.validators.validate_file_less_than_5mb])),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('tagged_animals', models.ManyToManyField(blank=True, to='animals.animals')),
            ],
            bases=(shelter_v11.commons.model_mixins.StrFromFieldsMixin, models.Model),
        ),
    ]
