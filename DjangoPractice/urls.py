"""DjangoPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# need to add include
from django.urls import path, include
# instead of making a urls.py in the app users we can import it directly to the project urls.py
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    # now when we open the browser and go to /blogs we will map to our urls file in blog folder which maps to our home view
    # path('blog/', include("blog.urls")),
    # if we want the homepage to be the blog then we can leave the path empty
    path('', include("blog.urls")),
    # site/register will take them to our app/views and use the register function, named it register
]
