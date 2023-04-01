from shelter_v11.animals.models import Animals


def get_pet_by_name_and_username(pet_slug, username):
    return Animals.objects.get(slug=pet_slug)