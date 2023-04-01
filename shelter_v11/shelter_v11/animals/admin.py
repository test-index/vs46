from django.contrib import admin

from shelter_v11.animals.models import Animals


@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    pass
