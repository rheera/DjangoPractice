# need to import redirect as well since, after successful sign up they should move to another page
from django.shortcuts import render, redirect
# django has a form class already, we don't need it now that we made our own
# from django.contrib.auth.forms import UserCreationForm
# importing flash messages, flash let's use see a one time message that is gone in the next request
# ex. messages.debug, messages.info, messages.success, messages.warning, messages.error
from django.contrib import messages
# need to inherit from the form we created
from .forms import UserRegisterForm

def register(request):
    # if we get a post request, we will instantiate a user creation form with the post data
    # we submit the registration form (it's a post update) --> if it isn't valid it drops down to return back to request page with the post information which is the username
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # checks if the form is valid when it's submitted
        if form.is_valid():
            # save the user into db
            form.save()
            username = form.cleaned_data.get('username')
            # since it is valid we'll send a success message
            messages.success(request, f"Account created for {username}!")
            return redirect("blog-home")
    # otherwise it'll just be an empty form
    else:
        # create a new instance of the form
        form = UserRegisterForm()
    # always need to pass request, then template name, then context
    return render(request, 'users/register.html', {'form': form})
