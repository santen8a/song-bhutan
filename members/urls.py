from django.urls import path
from . views import UserEditView, UserRegisterView, PasswordsChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
 
    path('register/',UserRegisterView.as_view(),name='register'),
    path('update/',UserEditView.as_view(),name='profile-edit'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))
    path('password/',PasswordsChangeView.as_view(),name='password-change'),


]

