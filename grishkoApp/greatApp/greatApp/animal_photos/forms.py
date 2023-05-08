from django import forms

from greatApp.animal_photos.models import AnimalPhotos
from greatApp.commons.forms_mixins import DisabledFormMixin
from greatApp.commons.models import PhotoLike, PhotoComment


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = AnimalPhotos
        exclude = ('publication_date',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = AnimalPhotos
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_animals.clear()  # many-to-many

            AnimalPhotos.objects.all() \
                .first().tagged_animals.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            self.instance.delete()

        return self.instance