from django.conf.urls import patterns, url
urlpatterns = patterns('app.views',
    url(r'export/(?P<id_user>[0-9]+)/', 'export_xls', name='export'),
    url(r'export$', 'export_xls', name='export'),
)
