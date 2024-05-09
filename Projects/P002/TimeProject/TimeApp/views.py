from django.shortcuts import render,HttpResponse
from datetime import datetime

def time_views(request):
    now=datetime.now()
    return HttpResponse(now)