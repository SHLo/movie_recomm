"""movie_recomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from main.views import IndexView
from main.views import MovieListView
from main.views import HistoryListView
from main.views import RatingView
from main.forms import UserCreateForm
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^register/$', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreateForm,
        success_url='/index/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),
    url('^list/$', MovieListView.as_view()),
    url('^history/$', HistoryListView.as_view()),
    url('^rating/$', RatingView.as_view()),
]
