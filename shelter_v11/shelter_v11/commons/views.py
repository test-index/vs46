import pyperclip as pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from shelter_v11.animal_photos.models import AnimalPhotos
from shelter_v11.commons.forms import PhotoCommentForm, SearchPhotosForm
from shelter_v11.commons.models import PhotoLike
from shelter_v11.commons.utils import get_user_liked_photos, get_photo_url, apply_likes_count, apply_user_liked_photo


def index(request):
    search_form = SearchPhotosForm(request.GET)
    searh_pattern = None

    if search_form.is_valid():
        searh_pattern = search_form.cleaned_data['animal_name']

    photos = AnimalPhotos.objects.all()

    if searh_pattern:
        photos = photos.filter(tagged_animals__name__icontains=searh_pattern)

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }

    return render(
        request,
        'test_template/home-page.html',
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


def comment_photo(request, photo_id):
    photo = AnimalPhotos.objects.filter(pk=photo_id).get()
    form = PhotoCommentForm(request.POST)
    zz = form
    # dd = form.cleaned_data
    gg = form.errors
    if form.is_valid(): # it is not valid !!!! #Todo check why not saving comments
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()
    return redirect('index')
