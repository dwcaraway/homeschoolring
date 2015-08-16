__author__ = 'dave'
from django.shortcuts import render

def ajax(request, ajax_code):

    context = {}
    return render(request=request, template_name="hes/ajax/%s.html" % ajax_code, context=context)
