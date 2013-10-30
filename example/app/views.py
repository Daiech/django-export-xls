# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from app.models import Book

def home(request):
    obj_list = Book.objects.all()
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))


@login_required
def export_xls(request, id_user=False):
    from export_xls.views import export_xlwt
    fields = ["id", "name", "author", "price"]
    if id_user:
        from django.contrib.auth.models import User
        _user = User.objects.get(pk=id_user)
        queryset = Book.objects.filter(author=_user)
        filename = "%ss-%s" %(_user.username, Book._meta.verbose_name_plural.lower())
    else:
        queryset = Book.objects.all()
        filename = Book._meta.verbose_name_plural.lower()
    try:
        return export_xlwt(filename, fields, queryset.values_list(*fields))
    except Exception, e:
        raise e

