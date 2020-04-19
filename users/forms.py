# need to make this file so we can add an e-mail field to the reigstration form
# need to inherit from the base form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# extends UserCreationForm
class UserRegisterForm(UserCreationForm):
    # EmailField(required=false) the argument by default is true, we'll leave it as default
    email = forms.EmailField()

    # model that the form interacts with is User, when it validates it makes a new user
    # when we do form save it'll save it to the User model
    class Meta:
        model = User
        # fields we want in the form and in what order
        # password1 is the first tie they type and password2 is the confirmation
        fields = ['username', 'email', 'password1', 'password2']
