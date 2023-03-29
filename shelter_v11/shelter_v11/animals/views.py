from django.shortcuts import render


def add_animal(request):
    return render(request, 'animals/animal-add-page.html')


def delete_animal(request, username, pet_name):
    return render(request, 'animals/animal-delete-page.html')


def details_animal(request, username, pet_name):
    return render(request, 'animals/animal-details-page.html')


def edit_animal(request, username, pet_name):
    return render(request, 'animals/animal-edit-page.html')