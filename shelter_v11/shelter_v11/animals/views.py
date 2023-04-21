from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shelter_v11.animals.forms import AnimalCreateForm, AnimalEditForm, AnimalDeleteForm
from shelter_v11.animals.models import Animals
from shelter_v11.animals.utils import get_animal_by_name_and_username
from shelter_v11.commons.utils import apply_likes_count, apply_user_liked_photo, is_owner


@login_required
def add_animal(request):
    if request.method == 'GET':
        form = AnimalCreateForm()
    else:
        form = AnimalCreateForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.user = request.user
            animal.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
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
            return redirect('details user', request.user.pk)

    context = {
        'form': form,
        'animal_slug': animal_slug,
        'username': username,
    }
    return render(request, 'animals/animal-delete-page.html', context)


def details_animal(request, username, animal_slug):
    animal = get_animal_by_name_and_username(animal_slug, username)
    photos = [apply_likes_count(photo) for photo in animal.animalphotos_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]


    context = {
        'animal': animal,
        'photos_count': animal.animalphotos_set.count(),
        'animal_photos': photos,
        'is_owner': animal.user == request.user,
    }

    return render(
        request,
        'animals/animal-details-page.html',
        context,
    )


def edit_animal(request, username, animal_slug):
    animal = Animals.objects \
        .filter(slug=animal_slug, user__username=username) \
        .get()

    if not is_owner(request, animal):
        return redirect('animal details', username=username, animal_slug=animal_slug)

    if request.method == 'GET':
        form = AnimalEditForm(instance=animal)
    else:
        form = AnimalEditForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal details', username=username, animal_slug=animal_slug)

    context = {
        'form': form,
        'animal_slug': animal_slug,
        'username': username,
    }

    return render(request, 'animals/animal-edit-page.html', context)