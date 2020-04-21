# copied from original urls.py, except we don't need the admin stuff
from django.urls import path
# . is the current directory
from . import views
from .views import PostListView

urlpatterns = [
    # we can leave the path empty, so the empty path is the home page
    # can name the path, want to be clear with the naming in case you have more than one app and they have their own "home"
    # good to leave the trailing / so if someone types about or about/ they'll both work fine
    # this is for our home function view, we're using our ListView instead
    # path('', views.home, name="blog-home"),
    # needs to be converted into a view
    path('', views.PostListView.as_view(), name="blog-home"),
    path('entries/', views.entries, name="blog-entries"),
    path('about/', views.about, name="blog-about"),
]
