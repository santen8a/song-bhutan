from calendar import c
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView,UpdateView,DeleteView
from . models import Category, Post
from django.urls import reverse
from . forms import SongCreateForm,SongUpdateForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'song/home.html'
    ordering = ['updated_date']


class SongDetailView(DetailView):
    model = Post
    template_name = 'song/detail_song.html'


class SongCreateView(CreateView):
    model = Post
    form_class = SongCreateForm
    template_name = 'song/create_song.html'
    # fields = '__all__'

    def get_success_url(self):
        return reverse('home')

class SongUpdateView(UpdateView):
    model = Post
    form_class = SongUpdateForm
    template_name = 'song/update_song.html'
    # fields = '__all__'

    def get_success_url(self):
        return reverse('home')

class SongDeleteView(DeleteView):
    model = Post
    template_name = 'song/delete_song.html'

    def get_success_url(self):
        return reverse('home')


class CategoryCreateView(CreateView):
    model = Category
    # form_class = CategoryCreateForm
    template_name = 'song/create_category.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')