# need to import redirect as well since, after successful sign up they should move to another page
from django.shortcuts import render, redirect
# django has a form class already, we don't need it now that we made our own
# from django.contrib.auth.forms import UserCreationForm
# importing flash messages, flash let's use see a one time message that is gone in the next request
# ex. messages.debug, messages.info, messages.success, messages.warning, messages.error
from django.contrib import messages
# need to inherit from the form we created
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# login required decorator, checks if a user is logged in to allow them on a certain page
from django.contrib.auth.decorators import login_required


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
            messages.success(request, f"{username}, your account has been created, now you can login!")
            # redirect users to login page
            return redirect("login")
    # otherwise it'll just be an empty form
    else:
        # create a new instance of the form
        form = UserRegisterForm()
    # always need to pass request, then template name, then context
    return render(request, 'users/register.html', {'form': form})


# profile page for users
@login_required
def profile(request):
    # this is run when we submit our form
    if request.method == "POST":
        # to populate form with current users info
        # these are model forms expecting to work on object, we can populate the forms by passing in an object
        # we can pass in an instance of the object it's expecting, so for user_update_form it'll be an instance of a user
        # request.POST passes in the POST data, and we leave the instances set so it knows what profile and user we want to update
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        # profile data has a picture file so we need to add that
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # need to check if both forms are valid then we'll save them
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f"Your profile has been updated!")
            # want to redirect here and not let it fall all the way down  because of POST GET redirect pattern
            # when you reload your browser after submitting a form and you get that popup are you sure you want to resubmit
            return redirect("profile")
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'users/profile.html', context)
