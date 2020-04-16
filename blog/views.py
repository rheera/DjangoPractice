from django.shortcuts import render
from django.http import HttpResponse


# Home handles traffic from the homepage of our blog
# takes in a request argument
# need to map home to a url in urls.py in the blog folder
def home(request):
    return HttpResponse("<h1>Blog Home</h1>")


def entries(request):
    return HttpResponse("<h1>Blog Entries</h1>")

def about(request):
    return HttpResponse("<h1>Blog About</h1>")
