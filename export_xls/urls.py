from django.conf.urls import patterns, url
urlpatterns = patterns('export_xls.views',
    url(r'^export_xls$', 'export_xlwt', name='export_xls'),
)
