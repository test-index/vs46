from django import forms

from greatApp.animals.models import Animals
from greatApp.commons.forms_mixins import DisabledFormMixin


class AnimalBaseForm(forms.ModelForm):
    class Meta:
        model = Animals

        fields = ('name', 'date_of_birth', 'personal_photo')

        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class AnimalCreateForm(AnimalBaseForm):
    pass


class AnimalEditForm(DisabledFormMixin, AnimalBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class AnimalDeleteForm(DisabledFormMixin, AnimalBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance