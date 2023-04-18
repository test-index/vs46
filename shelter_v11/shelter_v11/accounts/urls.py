from django.urls import path, include

from shelter_v11.accounts.views import SignInView, \
    SignUpView, UserDetailsView, UserEditView, UserDeleteView, SignOutView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('register/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='deletes user'),
    ])),
]