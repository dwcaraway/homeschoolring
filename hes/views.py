__author__ = 'dave'
from django.shortcuts import render

def ajax(request, ajax_code):
    return render(request=request, template_name="hes/ajax/%s.html" % ajax_code, context={})

def coming_soon(request):
    return render(request=request, template_name="hes/coming-soon.html", context={})
