from django.db import models
# need to import User since the profile will be a one to one relationship between the two
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # each profile has an image field where their profile pic is stored
    # default profile pic will be default.jpg
    # any uploaded profile pics will be stored to the profile_pics directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # any time we print out a profile it will print out profile object but we want it to be more specific
    def __str__(self):
        return f'{self.user.username} Profile'

