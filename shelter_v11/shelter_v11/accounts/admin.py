from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from shelter_v11.accounts.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
