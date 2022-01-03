from django.urls import path, include
from django.views.generic import TemplateView

from .views import AuthorListView, AuthorDetailView

app_name='blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html"), name='posts'),
    path('featured-posts/', TemplateView.as_view(template_name="blog/index.html"), name='featured-posts'),
    # path('authors/', TemplateView.as_view(template_name="blog/index.html"), name='authors'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]