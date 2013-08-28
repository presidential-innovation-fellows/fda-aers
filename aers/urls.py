from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from reports.api import ReportResource

report_resource = ReportResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aers.views.home', name='home'),
    # url(r'^aers/', include('aers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^report/', include("reports.urls")),
    url(r'^api/', include(report_resource.urls)),
)
