from django.shortcuts import render
# django has a form class already
from django.contrib.auth.forms import UserCreationForm

def register(request):
    # create a new instance of the form
    form = UserCreationForm()
    # always need to pass request, then template name, then context
    return render(request, 'users/register.html', {'form': form})
