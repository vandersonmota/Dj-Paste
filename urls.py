from django.conf.urls.defaults import *
from djpaste.models import Snippet
from djpaste.views import new
from djpaste.views import view_snippet
from djpaste.views import reply
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
    (r'^$', new),
    (r'^view/(?P<id>\d+)', view_snippet),
    (r'^reply/(?P<id>\d+)', reply),
   
)
