from django.db import models
# need to import User since the profile will be a one to one relationship between the two
from django.contrib.auth.models import User
# need pillow to resize image
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # each profile has an image field where their profile pic is stored
    # default profile pic will be default.jpg
    # any uploaded profile pics will be stored to the profile_pics directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # any time we print out a profile it will print out profile object but we want it to be more specific
    def __str__(self):
        return f'{self.user.username} Profile'


    # method that already exists in parent class, ran after our model is saved
    # this method might not be the most efficient to resize photos, but it's simple
    def save(self):
        # this runs our normal save function
        super().save()
        # opens image of the current instance
        img = Image.open(self.image.path)
        # if the height or width of the image is greater than 300 resize it to 300 by 300
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
