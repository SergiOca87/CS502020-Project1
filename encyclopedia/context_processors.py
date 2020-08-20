from django import forms

class NewTaskForm(forms.Form):
    search = forms.CharField(label="Search")
    
def add_variable_to_context(request):
    return {
        "form": NewTaskForm()
    }