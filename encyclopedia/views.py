from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util

class NewTaskForm(forms.Form):
    search = forms.CharField()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def results(request):
    return render(request, "encyclopedia/results.html", {
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
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            searchQuery = util.get_entry( form.cleaned_data["search"] )
            if searchQuery == None :
                return render(request, "encyclopedia/results.html", {
                    "query": util.list_entries()
                })
            else :
                return render(request, "encyclopedia/results.html", {
                    searchQuery
                })
        else:
            return render(request, "/", {
                "form": form
            })

    else:
        return render(request, "/", {
            "form": NewTaskForm()
        })    



# def entry(request, entry_name):
#     return render(request, "encyclopedia/entry.html", {
#         "entry_name": entry_name
#     })

