from django.urls import path
import users.views as uv


urlpatterns = [
    path('create', uv.create_account),
    path('login', uv.login),
    path('create_profile', uv.create_profile),
    path('update_profile', uv.update_profile),
    path('view_profile', uv.view_profile),
    path('change_password', uv.change_password),
]
