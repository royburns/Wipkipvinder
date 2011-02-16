from django.conf.urls.defaults import *
from views import index, themap

urlpatterns = patterns('',
    (r'^public/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': 'public/'}),
    url(r'^/?$', index),
    url(r'^themap?$', themap),
)