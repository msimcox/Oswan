"""Treasuregram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from main import views

urlpatterns = [
    url(r'^$', views.index),

    # Can't figure out how to use two views at the same URL. ie how does Djangjo know whether to use detail1 vs detail2 view at this url: http://localhost:8000/1/
    #Disabling detail1 for now
    #url(r'^([0-9]+)/$', views.detail1, name = 'detail1'),

    url(r'^([0-9]+)/$', views.detail2, name = 'detail2'),
    url(r'^post_url/$', views.post_moto, name='post_moto'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
]