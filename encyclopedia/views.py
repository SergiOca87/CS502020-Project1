from django.shortcuts import render

from . import util


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

# def entry(request, entry_name):
#     return render(request, "encyclopedia/entry.html", {
#         "entry_name": entry_name
#     })

