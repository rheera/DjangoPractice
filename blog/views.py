from django.shortcuts import render
# don't need the HttpResponse import when using templates, since it uses render
from django.http import HttpResponse
# import post class as a table
from .models import Post
# importing list view for home page
# you can split up a long import by surrounding the imports with brackets
from django.views.generic import ListView, DetailView, CreateView


# Create view to post a single blog post, going to create a form we just need to provide the fields
class PostCreateView(CreateView):
    model = Post
    # don't need to add author since it'll be user that's signed in, and date will be automatic
    fields = ['title', 'content']

    # need to override form_valid method to make the user that's signed in the author
    def form_valid(self, form):
        # before you submit the form take that instance and set the author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


# Detail view to view a single blog post
class PostDetailView(DetailView):
    model = Post


# new list view for posts inheriting from ListView
class PostListView(ListView):
    # tells list view what model to query
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    # need to tell it what variable we will be looping over
    # by default list view calls it object_list, we have it called posts in the function
    # we can go to template to change posts to object_list, or set a variable
    context_object_name = 'posts'
    # order posts so that newest is at the top
    ordering = ['-date_posted']


# Home handles traffic from the homepage of our blog
# takes in a request argument
# need to map home to a url in urls.py in the blog folder


def home(request):
    # dictionary for the data inputted, with the key posts
    # pass this as the third argument for render
    # now it can be used by our templates
    context = {
        # instead of using the dummy data import it from the database
        # 'posts': posts
        'posts': Post.objects.all()
    }
    # you can fit an entire html page in this http response
    # better to use templates
    # to use templates create a new folder in the blog app directory called templates
    # Django looks for a templates subdirectory in each app
    # need to create a folder inside templates with the name of the app (weird)
    # Project/App/Templates/App/template.html
    # return HttpResponse("<h1>Blog Home</h1>")
    # we can load the template and pass it through our HttpResponse but that's the long way
    # instead use the Django Shortcuts module, which is why Django already imported it for us

    # render takes in the request and template name, third argument is the context to pass info into the template
    # still returning an HttpResponse in the background
    return render(request, 'blog/home.html', context)


def entries(request):
    return HttpResponse("<h1>Blog Entries</h1>")


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
