#!usr/bin/env python
#_*_ coding:utf-8 _*_

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['isshow'] = False
    context['hello'] = "Hello World!"
    context['bye'] = "Good Bye!"
    context['athletes'] = [{'name':'Ton'},{'name':'Tom'}]
    return render(request,"hello.html",context)