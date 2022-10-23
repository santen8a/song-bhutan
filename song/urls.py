from django.contrib import admin
from django.urls import path
from . views import CategoryCreateView, HomeView, SongDeleteView, SongDetailView, SongCreateView, SongUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),


    path('song/view/<int:pk>', SongDetailView.as_view(), name='detail-song'),
    path('song/create/', SongCreateView.as_view(), name='create-song'),
    path('song/update/<int:pk>', SongUpdateView.as_view(), name='update-song'),
    path('song/delete/<int:pk>', SongDeleteView.as_view(), name='delete-song'),

    path('category/create', CategoryCreateView.as_view(), name='create-category'),


]
