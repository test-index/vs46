from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from shelter_v11.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(CreateView):
    # TODO CHECK IF YOU REMOVE USERNAME, MAIL ETC FROM THE TEMplate If THEY Will show
    zz =1
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserEditView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender',)

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy('details user', kwargs={'pk':user_id})


class UserDetailsView(DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['animals_count'] = self.object.animals_set.count()

        photos = self.object.animalphotos_set \
            .prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context



