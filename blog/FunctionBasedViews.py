from django.shortcuts import render
# don't need the HttpResponse import when using templates, since it uses render
from django.http import HttpResponse
# import post class as a table
from .models import Post


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
