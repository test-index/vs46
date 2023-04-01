from django.urls import path

from shelter_v11.commons.views import index

urlpatterns = (
    path('', index, name='index'),
)