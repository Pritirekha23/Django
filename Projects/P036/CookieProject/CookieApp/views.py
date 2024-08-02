from django.shortcuts import render
from django.http import HttpResponse

def set_cookie_view(request):
    res=HttpResponse("Cookie is set")
    res.set_cookie('name','Priti',max_age=10)
    return res

def get_cookie_view(request):
    name=request.COOKIES['name']
    res=HttpResponse('Cookie name is ' +name)
    return res

def delete_cookie_view(request):
    res=HttpResponse("Cookie is deleted")
    res.delete_cookie('name')
    return res

