from django.contrib import admin
# import what you want to register
from .models import Post

# Register your models here.
# register it
admin.site.register(Post)
