from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

class NewTaskForm(forms.Form):
    createFormTitle = forms.CharField(label="Title")
    createFormText = forms.CharField(label="Text", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

    
def entry(request, entry_name):
    entry = util.get_entry( entry_name )
    if entry == None :
        return render(request, "encyclopedia/404.html")
    else :
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry( entry_name ),
            "title": entry_name
        })

def search(request):
    # Get the value of the URL query string from the search form
    searchQuery = request.GET['q']
    searchResult = util.get_entry( searchQuery )

    if( searchResult == None):
        # Get all existing entries
        entries = util.list_entries()

        # Use a lambda function synthax to filter through the list, compare the searchQuery in lowercase
        # with each of the existing items in the entries list
        filteredEntries = list( filter(lambda entry: searchQuery.lower() in entry.lower(), entries ))
       
        # Return the search page with matching results
        return render(request, "encyclopedia/search.html", {
            "entries": filteredEntries
        })
    else : 
        # If search query match, simply return that entry page
        return render(request, "encyclopedia/entry.html", {
            "entry": searchResult,
            "title": searchQuery
        });

# def resuts(request):
#     return render(request, "encyclopedia/results.html", {
#         "entries": entries
#     })

def create(request):
    if(request.method == 'POST'):
        form = NewTaskForm(request.POST)
        if form.is_valid():
            createFormTitle = form.cleaned_data['createFormTitle']
            createFormText = form.cleaned_data['createFormText']

            # First check if the entry already exists
            if( util.get_entry( createFormTitle ) is not None):
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    "error": 'Sorry, the entry already exists'
                })
            else :
                util.save_entry(createFormTitle, createFormText)
                return render(request, "encyclopedia/entry.html", {
                    "entry": util.get_entry( createFormTitle ),
                    "title": createFormTitle
                });
            # append new entry to the list we retrieve from util.get_entries...
            # render index.html with new entry
        else:
            return render(request, 'encyclopedia/create.html', {
                "form": form
            })
    else:
        return render(request, "encyclopedia/create.html", {
            "form": NewTaskForm()
        })
