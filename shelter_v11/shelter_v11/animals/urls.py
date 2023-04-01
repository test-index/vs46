from django.urls import path, include

from shelter_v11.animals.views import add_animal, details_animal, edit_animal, delete_animal

urlpatterns = [
    path('admin/', add_animal, name='add animal'),
    path('<str:username>/animal/<slug:animal_name>/', include([
        path('', details_animal, name='animal details'),
        path('edit/', edit_animal, name='edit details'),
        path('delete/', delete_animal, name='delete details'),
    ])),
]
