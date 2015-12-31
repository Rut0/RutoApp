from django.conf.urls import url

from . import views

urlpatterns = [
    # /blog/
    url(r'^$', views.index, name='index'),
    # /blog/<id>
    url(r'^(?P<id>[0-9]+)/$', views.id, name='id'),
    # /blog/<word>
    url(r'^(?P<word>.*)/$', views.word, name='word'),
]
