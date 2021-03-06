"""twitty_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movieratings.views import top_twenty_views, movie_page, all_of_the_movies, every_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_of_the_movies, name="index_view"),
    url(r'^toptwenty/', top_twenty_views, name="top_twenty"),
    url(r'^(?P<pk>\d+)$', movie_page, name="movie"),
    url(r'^user/(?P<pk>\d+)$',every_user, name="all_users")
]
