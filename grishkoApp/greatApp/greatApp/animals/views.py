from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from greatApp.animals.forms import AnimalCreateForm, AnimalDeleteForm, AnimalEditForm
from greatApp.animals.models import Animals
from greatApp.commons.utils import get_animal_by_name_and_username, apply_likes_count, apply_user_liked_photo, is_owner


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