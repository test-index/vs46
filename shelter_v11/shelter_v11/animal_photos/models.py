from django.core.validators import MinLengthValidator
from django.db import models

from shelter_v11.animal_photos.validators import validate_file_less_than_5mb
from shelter_v11.animals.models import Animals
from shelter_v11.commons.model_mixins import StrFromFieldsMixin


class AnimalPhotos(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location',)
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='animal_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_animals = models.ManyToManyField(
        Animals,
        blank=True,
    )
