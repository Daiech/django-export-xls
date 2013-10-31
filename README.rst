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

2. Be sure to have the MEDIA_ROOT and MEDIA_URL vars defined. eg::

      import os
      MEDIA_ROOT = os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'media'])
      MEDIA_URL = '/media/'


3. The only thing that you must to do is create an excel file is::

      * Define a name for your file
      * Define a Python list with the fields you want in your excel (xls headers).
      * Create a python list with the values ​​you want to add to your xls file.


How to use
----------

* Import the function::

      from export_xls.views import export_xlwt

* 'export_xlwt' function needs:

    3 mandatory parameters::

      filename
      fields
      values_list

    2 optional parameters::

      save   : save the xls file on settings.MEDIA_ROOT
      folder : save the xls file on settings.MEDIA_ROOT/folder 

* 'export_xlwt' function return the string::

      MEDIA_URL + folder + filename 
      eg: /media/xls/filename.xls

eg::

      from export_xls.views import export_xlwt
      return export_xlwt(filename, fields, values_list, save=True, folder="xls/")


Example
-------

view the real example. Clone de github repo::

      git clone https://github.com/Daiech/django-export-xls
      cd django-export-xls/example
      python manage.py runserver


Credentians for database::

      * user: daiech
      * pass: 1
