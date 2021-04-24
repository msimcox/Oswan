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
    url(r'^login/$', views.login_view, name='Login'),
    url(r'^logout/$', views.logout_view, name='Logout'),
    url(r'^like_motorcycle/$', views.like_motorcycle, name='like_motorcycle' ),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
]