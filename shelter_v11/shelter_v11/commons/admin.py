from django.contrib import admin

from shelter_v11.commons.models import PhotoComment, PhotoLike


@admin.register(PhotoComment)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoLike)
class PhotoLike(admin.ModelAdmin):
    pass
