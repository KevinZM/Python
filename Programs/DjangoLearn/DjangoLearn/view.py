#!/usr/bin/python
#coding: utf-8
import datetime
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import MySQLdb

def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
    return HttpResponse("我的主页!")

def date_time(request):
    date_time = datetime.datetime.now()
    #now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date':now}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date':date_time})
    #return render_to_response('current_datetime.html',locals())

def date_head(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)