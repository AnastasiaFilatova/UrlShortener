from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'shortener.views.startpage', name='startpage'),
    url(r'^$', 'views.get_base_url',
        name='shortener.views.get_base_url'),
]
