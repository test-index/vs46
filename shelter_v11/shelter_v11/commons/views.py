import pyperclip as pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from shelter_v11.animal_photos.models import AnimalPhotos
from shelter_v11.commons.models import PhotoLike
from shelter_v11.commons.utils import get_user_liked_photos, get_photo_url, apply_likes_count, apply_user_liked_photo


def index(request):
    photos = [apply_likes_count(photo) for photo in AnimalPhotos.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }

    return render(
        request,
        'common_all/home-page.html',
        context,
    )


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))
