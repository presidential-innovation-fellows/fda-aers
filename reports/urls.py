from django.conf.urls import patterns
from django.conf.urls import url

from .views import ReportDetailView

urlpatterns = patterns('',
    url(r'^(?P<slug>[-_\w]+)/$', ReportDetailView.as_view(), name="detail")
)