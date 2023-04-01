from django.contrib import admin

from shelter_v11.animal_photos.models import AnimalPhotos


@admin.register(AnimalPhotos)
class AnimalPhotosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date')

    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No pets'
