"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings

from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from app2.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),



    #url(r'^$',TemplateView.as_view(template_name='introduction.html'), name="home"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$',intro),
    # url(r'^django/(\w+)/$', django_tutorial_new),


    url(r'^introduction/(\w+)/$',intro),
    url(r'^registration/(\w+)/$',registration),
    url(r'^login/(\w+)/$',login),
    url(r'^logout/(\w+)/$', logout),

    url(r'^django/windows/$',windows),
    url(r'^django/linux/$', linux),
    url(r'^django/models/$',model1),
    url(r'^django/views/$', myview, name='django_view'),
    url(r'^search_post/$', search_status),
    url(r'^django/forms/$', myforms),
    url(r'^django/bootstrap/$',bootstrap1),
    url(r'^django/more_practice/$', combo),


    url(r'^login//$', login_intro),
    url(r'^registration//$',registration_intro),
    url(r'^logout//$', logout_intro)
]
