from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:entry_name>/", views.entry, name="entry"),
    path("encyclopedia/search/", views.search, name="search"),
    path("encyclopedia/results/", views.results, name="results")
]
