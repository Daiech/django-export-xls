from django.http import HttpResponse
import xlwt
from datetime import datetime, date
from django.template.defaultfilters import slugify
from django.conf import settings


def export_xlwt(filename, fields, values_list, save=False, folder=""):
    """export_xlwt is a function based on http://reliablybroken.com/b/2009/09/outputting-excel-with-django/"""
    filename = slugify(filename)
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet(filename)

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    for j, f in enumerate(fields):
        sheet.write(0, j, fields[j])

    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style

            sheet.write(row + 1, col, val, style=style)

    if not save:
        response = HttpResponse(mimetype='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s.xls' % filename
        book.save(response)
        return response
    else:
        dirpath = '%s/%s' % (settings.MEDIA_ROOT, folder)
        if folder != "":
            import os
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
        filepath = '%s%s.xls' % (dirpath, filename)
        book.save(filepath)
        return "%s%s%s.xls" % (settings.MEDIA_URL, folder, filename)
