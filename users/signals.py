# this is a signal that gets fired after an object is saved
# we want a post_save signal when a user is created
from django.db.models.signals import post_save
# User is called the sender, it is sending the signal
from django.contrib.auth.models import User
# need a receiver to do a function after receiving the signal
from django.dispatch import receiver
# need profile since we'll be creating a profile
from .models import Profile


# when a user is saved send this signal, signal will be received by this function
# this function takes all these arguments that the post_save signal passed to it
# post_save is the signal
@receiver(post_save, sender=User)
# instance is the user
def create_profile(sender, instance, created, **kwargs):
    # if that user was created then create a profile object, with the user = the instance of that user
    if created:
        Profile.objects.create(user=instance)


# saves the profile every time a user gets saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
