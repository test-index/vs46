import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from greatApp.animal_photos.models import AnimalPhotos
from greatApp.commons.forms import SearchPhotosForm, PhotoCommentForm
from greatApp.commons.models import PhotoLike
from greatApp.commons.utils import apply_likes_count, apply_user_liked_photo, get_photo_url


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
        'test_templ/home-page.html',
        context,
    )


@login_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects.\
        filter(photo_id=photo_id, user_id=request.user.pk)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


@login_required
def comment_photo(request, photo_id):
    photo = AnimalPhotos.objects.filter(pk=photo_id).get()
    form = PhotoCommentForm(request.POST)
    zz = form
    # dd = form.cleaned_data
    user_id = request.user.pk

    gg = form.errors
    if form.is_valid(): # it is not valid !!!! #Todo check why not saving comments
        comment = form.save(commit=False)
        comment.photo = photo
        comment.user_id = user_id
        comment.save()
    return redirect('index')
