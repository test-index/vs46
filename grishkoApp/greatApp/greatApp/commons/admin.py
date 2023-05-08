from django.contrib import admin
from greatApp.commons.models import PhotoComment, PhotoLike


@admin.register(PhotoComment)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoLike)
class PhotoLike(admin.ModelAdmin):
    pass
