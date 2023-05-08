from django.urls import path

from greatApp.commons.views import index, comment_photo, like_photo, share_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),
    path('share/<int:photo_id>/', share_photo, name='share photo'),
)