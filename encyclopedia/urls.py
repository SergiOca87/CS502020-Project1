from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:entry_name>/", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("results", views.results, name="results")
]
