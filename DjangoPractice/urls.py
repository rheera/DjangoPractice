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
# these are views DJango provides for logins/logouts, any time you import views use as so it's specific
from django.contrib.auth import views as auth_views
# serving static media content during development, taken from Django documentation
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    # now when we open the browser and go to /blogs we will map to our urls file in blog folder which maps to our home view
    # path('blog/', include("blog.urls")),
    # if we want the homepage to be the blog then we can leave the path empty
    path('', include("blog.urls")),
    # site/register will take them to our app/views and use the register function, named it register

    # these are class based views
    # as_view was looking for a template in crispy_forms/registration/login.html by default
    # we passed an argument for template to be in our users folder
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # redirect user to homepage if they try to access login page, while being logged in
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    # by default logout will take you to admin logout page, which we don't want, don't want unnecessary access to admin page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    # path that will send password reset instructions to the users email
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    # page for if the password reset form has been submitted correctly
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    # expects those two parameters uid and token, view is PasswordResetConfirm
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # password reset complete
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
# taken from Django documentation for serving static media during development
# if isn't needed just makes it clear that we're only doing this if we're in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
