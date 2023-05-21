from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from greatApp.animals.models import Animals
from greatApp.commons.model_mixins import StrFromFieldsMixin
from greatApp.commons.validators import validate_file_less_than_5mb

UserModel = get_user_model()


class AnimalPhotos(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location',)
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = cloudinary_models.CloudinaryField(
        null=False,
        blank=True,
        # validators=(validate_file_less_than_5mb,),
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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )