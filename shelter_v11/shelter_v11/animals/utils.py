from shelter_v11.animals.models import Animals


def get_animal_by_name_and_username(animal_slug, username):
    return Animals.objects.get(slug=animal_slug)