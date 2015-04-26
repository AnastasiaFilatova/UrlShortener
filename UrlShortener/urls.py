from django.conf.urls import url
from shortener.views import handle_form, redirect_url

urlpatterns = [
    url(r'^$', handle_form),
    url(r'^.*$', redirect_url)
]
