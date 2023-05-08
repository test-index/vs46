from greatApp.animals.models import Animals
from greatApp.commons.models import PhotoLike


def get_user_liked_photos(photo_id):
    return PhotoLike.objects.filter(photo_id=photo_id)


def get_photo_url(request, photo_id):

    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def is_owner(request, obj):
    return request.user == obj.user


def get_animal_by_name_and_username(animal_slug, username):
    return Animals.objects.filter(slug=animal_slug, user__username=username) \
        .get()