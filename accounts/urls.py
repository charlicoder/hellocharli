from django.urls import include, path

from . import views

# urlpatterns = [
#     path('', views.PersonListView.as_view(), name='person_changelist'),
#     path('add/', views.PersonCreateView.as_view(), name='person_add'),
#     path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
# ]


urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]
