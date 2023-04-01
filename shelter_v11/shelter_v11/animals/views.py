from django.shortcuts import render

from shelter_v11.animals.utils import get_pet_by_name_and_username
from shelter_v11.commons.utils import apply_likes_count, apply_user_liked_photo


def add_animal(request):
    return render(request, 'animals/animal-add-page.html')


def delete_animal(request, username, pet_name):
    return render(request, 'animals/animal-delete-page.html')


def details_animal(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context,
    )


def edit_animal(request, username, pet_name):
    return render(request, 'animals/animal-edit-page.html')