from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Author, Post, Publisher

from suit_dashboard.views import DashboardView


class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = 'This is skfwjer text..!'

        return context


class HomeView(DashboardView):
    pass
