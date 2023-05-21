from django.urls import include, path
from .signals import *
from greatApp.accounts.views import SignInView, SignUpView, SignOutView, \
UserDetailsView, UserEditView, UserDeleteView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logou/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='deletes user'),
    ])),
]

