from django.contrib import admin

from greatApp.animal_photos.models import AnimalPhotos


@admin.register(AnimalPhotos)
class AnimalPhotosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'animals')

    @staticmethod
    def animals(current_photo_obj): # this is from the decorator and it takes the current photo obj because it takes it from AnimalPhotos
        tagged_animals = current_photo_obj.tagged_animals.all()
        if tagged_animals:
            return ', '.join(p.name for p in tagged_animals)
        return 'No pets'

