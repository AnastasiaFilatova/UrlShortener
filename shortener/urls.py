from django.conf.urls import include, url, patterns
from shortener.views import get_base_url

urlpatterns = patterns('',
                       url(r'^$', get_base_url),
                       )
