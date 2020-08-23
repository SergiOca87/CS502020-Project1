from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:entry_name>/", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("encyclopedia/edit/<str:entry_name>", views.edit, name="edit"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("create", views.create, name="create")
]
