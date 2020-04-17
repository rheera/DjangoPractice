from django.db import models
# for date_posted default, allows us to take a datetime that takes timezones into consideration
from django.utils import timezone
# for author, using the user table Django created
# Users will author posts, 1 to many relationship, 1 user can make many posts, a post can only be made by one author
from django.contrib.auth.models import User


# We're going to make a post class to handle our blog posts that inherits from models class
# each class will be it's own table in the database
# each attribute will be a different field in the database
class Post(models.Model):
    # title of the post, with a max length of 100 characters, default max for CharField is 255
    title = models.CharField(max_length=100)
    # textfield and charfield is similar but unrestricted
    content = models.TextField()
    # few options for date_posted
    # can use DateTimeField(auto_now=True) update date posted to current date time, every time post is updated, good for last modified
    # DateTimeField(auto_now_add=True) only updates date when the object is uploaded, but you can't change it afterwards
    # we need to import a Django utility for this default
    # we don't put parenthesis after timezone.now() because we don't want it to execute there, we want the function passed
    date_posted = models.DateTimeField(default=timezone.now)
    # author will be a user, which we already have a table/class for since Django made that
    # Use foreign key function to get the user from the other table
    # need to add the on_delete variable so Django knows what to do if the user gets deleted
    # Cascade means that if a user is deleted delete their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # need to make this so that when we query our posts they'll give us the title
    def __str__(self):
        return self.title
