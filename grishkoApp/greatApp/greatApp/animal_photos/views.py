from django.shortcuts import render, redirect
from django.urls import reverse

from greatApp.animal_photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from greatApp.animal_photos.models import AnimalPhotos
from greatApp.commons.utils import get_user_liked_photos


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect('details photo', pk=photo.pk)
    context = {
        'form': form,
    }
    return render(request, 'animal_photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = AnimalPhotos.objects.filter(pk=pk) \
        .get()
    user_pk = request.user.pk
    context = {
        'user_pk': user_pk,
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photos(pk),
        'likes_count': photo.photolike_set.count(), # manager, reverse rel, get all the likes for the photo
    }
    return render(request, 'animal_photos/photo-details-page.html', context)


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_path, context)


def edit_photo(request, pk):
    request.method = 'POST'
    photo = AnimalPhotos.objects.filter(pk=pk) \
        .get()
    return get_post_photo_form(
        request,
        PhotoEditForm(request.POST or None, instance=photo),
        success_url=reverse('index'),
        template_path='animal_photos/photo-edit-page.html',
        pk=pk,
    )


def delete_photo(request, pk):
    photo = AnimalPhotos.objects.filter(pk=pk) \
        .get()
    return get_post_photo_form(
        request,
        PhotoDeleteForm(request.POST or None, instance=photo),
        success_url=reverse('index'),
        template_path='animal_photos/photo-delete-page.html',
        pk=pk,
    )

