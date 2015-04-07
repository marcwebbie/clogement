from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from cahiers.api import (
    CahierResource,
    PaysResource,
    LogementResource,
    VilleResource
)


v1_api = Api(api_name='v1')
v1_api.register(CahierResource())
v1_api.register(PaysResource())
v1_api.register(VilleResource())
v1_api.register(LogementResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
