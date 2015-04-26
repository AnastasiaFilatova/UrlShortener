from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'shortener.views.get_base_url'),
]
