from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

class NewTaskForm(forms.Form):
    searchForm = forms.CharField(label="Search")

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
    # For i in entries(list of all entries), find the matching ones 
    # Watch lecture part about query strings and capturing that...
    searchQuery = request.GET['q']
    searchResult = util.get_entry( searchQuery )

    if( searchResult == None):
        entries = util.list_entries()
        filteredEntries = list( filter(lambda entry: searchQuery in entry, entries ))
        print(f"entry in... {filteredEntries} ")
        return render(request, "encyclopedia/index.html");
    else : 
        return render(request, "encyclopedia/entry.html", {
            "entry": searchResult,
            "title": searchQuery
        });
    # if request.method == "POST":
    #     form = NewTaskForm(request.POST)
    #     if form.is_valid():
    #         searchForm = form.cleaned_data["searchForm"]
    #         searchQuery = util.get_entry( searchForm )
    #         if searchQuery  == None :
    #             return render(request, "encyclopedia/index.html", {
    #                 "entries": util.list_entries(),
    #                 "form": form
    #             })
    #         else :
    #             return render(request, "encyclopedia/entry.html", {
    #                 "entry": searchQuery,
    #                 "title": searchForm
    #             })
    #     else:
    #         return render(request, "encyclopedia/index.html", {
    #             "entries": util.list_entries(),
    #             "form": form
    #         })

    # else:
    #     return render(request, "encyclopedia/index.html", {
    #         "form": NewTaskForm()
    #     })    



# def entry(request, entry_name):
#     return render(request, "encyclopedia/entry.html", {
#         "entry_name": entry_name
#     })

