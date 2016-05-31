from django.conf.urls import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^codigofacilito/blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^codigofacilito/admin/', include(admin.site.urls)),
)
