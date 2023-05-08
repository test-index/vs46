from django.contrib import admin

from greatApp.animals.models import Animals


@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    pass
