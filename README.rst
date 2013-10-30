=================
Django Export XLS
=================

Django Export XLS is a simple Django app to export data to a xls file.

Detailed documentation is in the "docs" directory.

Instalation
-----------

	  $ pip install django-export-xls


Quick start
-----------

1. Add "export_xls" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'export_xls',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^export_xls/', include('export_xls.urls')),

