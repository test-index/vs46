from django.shortcuts import render


def add_photo(request):
    return render(request, 'animal_photos/photo-add-page.html')


def details_photo(request, pk):
    return render(request, 'animal_photos/photo-details-page.html')


def edit_photo(request, pk):
    return render(request, 'animal_photos/photo-edit-page.html')