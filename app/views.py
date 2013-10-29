# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from app.models import Book

def home(request):
    obj_list = Book.objects.all()
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))


@login_required
def export_xls(request):
    from export_xls.views import export_xlwt
    fields = ["id", "name", "author", "price"]
    queryset = Book.objects.filter(author=request.user)
    try:
        return export_xlwt(Book, fields, queryset.values_list(*fields))
    except Exception, e:
        raise e

