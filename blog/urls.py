# copied from original urls.py, except we don't need the admin stuff
from django.urls import path
# . is the current directory
from . import views
# don't think I need this since above line is importing entire views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
)

urlpatterns = [
    # we can leave the path empty, so the empty path is the home page
    # can name the path, want to be clear with the naming in case you have more than one app and they have their own "home"
    # good to leave the trailing / so if someone types about or about/ they'll both work fine
    # this is for our home function view, we're using our ListView instead
    # path('', views.home, name="blog-home"),
    # needs to be converted into a view
    path('', views.PostListView.as_view(), name="blog-home"),
    # we need an url that contains a variable since we have to go to blog1 or blog 2
    # <pk> is for the primary key variable, int: pk means we expect pk to only be ints so people can't put strings and stuff
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="post-delete"),
    # need to include pk for update as well so we know which post we are updating
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="post-update"),
    path('post/new/', views.PostCreateView.as_view(), name="post-create"),
    path('entries/', views.entries, name="blog-entries"),
    path('about/', views.about, name="blog-about"),
    path('user/<str:username>', views.UserPostListView.as_view(), name="user-post"),
]
