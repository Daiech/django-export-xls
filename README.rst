=================
Django Export XLS
=================

Django Export XLS is a simple Django app to export data to a xls file.

Detailed documentation is in the "docs" directory on github https://github.com/Daiech/django-export-xls

Instalation
-----------

1. Install from PyPi::

      $ pip install django-export-xls


Quick start
-----------

1. Add "export_xls" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'export_xls',
      )


2. The only thing that you must to do is create an excel file is::

      * Define a name for your file
      * Define a Python list with the fields you want in your excel (xls headers).
      * Create a python list with the values ​​you want to add to your xls file.


How to use
----------

* Import function::

      from export_xls.views import export_xlwt

* export_xlwt receive:

  3 mandatory parameters::

      filename
      fields
      values_list

  2 optional parameters::

      save   : save the xls file on settings.MEDIA_ROOT
      folder : save the xls file on settings.MEDIA_ROOT/folder


Example
-------
clone de github repo::

      git clone https://github.com/Daiech/django-export-xls
      cd django-export-xls/example
      python manage.py runserver


Credentians for database:

* user: daiech
* pass: 1
