from django import forms

from greatApp.commons.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment'
                },

            ),
            # 'required id': None,
        }


class SearchPhotosForm(forms.Form):
    animal_name = forms.CharField(
        max_length=50,
        required=False,
    )
