from django.shortcuts import render, redirect

from shelter_v11.animals.forms import AnimalCreateForm, AnimalEditForm, AnimalDeleteForm
from shelter_v11.animals.models import Animals
from shelter_v11.animals.utils import get_animal_by_name_and_username
from shelter_v11.commons.utils import apply_likes_count, apply_user_liked_photo


def add_animal(request):
    if request.method == 'GET':
        form = AnimalCreateForm()
    else:
        form = AnimalCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': AnimalCreateForm(),
    }
    return render(request, 'animals/animal-add-page.html', context)


def delete_animal(request, username, animal_slug):
    animal = Animals.objects \
        .filter(slug=animal_slug) \
        .get()

    if request.method == 'GET':
        form = AnimalDeleteForm(instance=animal)
    else:
        form = AnimalDeleteForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'animal_slug': animal_slug,
        'username': username,
    }
    return render(request, 'animals/animal-delete-page.html', context)


def details_animal(request, username, ainmal_slug):
    animal = get_animal_by_name_and_username(ainmal_slug, username)
    photos = [apply_likes_count(photo) for photo in animal.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'animal': animal,
        'photos_count': animal.photo_set.count(),
        'animal_photos': photos,
    }

    return render(
        request,
        'animals/animal-details-page.html',
        context,
    )


def edit_animal(request, username, animal_slug):
    animal = Animals.objects \
        .filter(slug=animal_slug) \
        .get()

    if request.method == 'GET':
        form = AnimalEditForm(instance=animal)
    else:
        form = AnimalEditForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, animal_slug=animal_slug)

    context = {
        'form': form,
        'animal_slug': animal_slug,
        'username': username,
    }

    return render(request, 'animals/animal-edit-page.html', context)