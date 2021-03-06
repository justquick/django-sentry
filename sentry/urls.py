import os

from django.conf import settings
from django.conf.urls.defaults import *
from django.utils.hashcompat import md5_constructor

from feeds import MessageFeed, SummaryFeed
import views

hashed_secret = md5_constructor(settings.SECRET_KEY).hexdigest()

SENTRY_ROOT = os.path.dirname(__file__) 

urlpatterns = patterns('',
    url(r'^feeds/%s/messages.xml$' % hashed_secret, MessageFeed(), name='sentry-feed-messages'),
    url(r'^feeds/%s/summaries.xml$' % hashed_secret, SummaryFeed(), name='sentry-feed-summaries'),
    url(r'^group/(\d+)$', views.group, name='sentry-group'),
    url(r'^$', views.index, name='sentry'),
    url(r'^jsapi/$', views.ajax_handler, name='sentry-ajax'),
    url(r'^_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(SENTRY_ROOT, 'media')}, name='sentry-media'),
)
