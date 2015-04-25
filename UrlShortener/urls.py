from django.conf.urls import include, url
#from django.contrib import admin
from shortener import views

urlpatterns = [

    #### Start page ####
    url(r'^$', 'shortener.views.startpage', name='startpage'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
