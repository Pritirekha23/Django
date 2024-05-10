from django.shortcuts import render,HttpResponse

def education_view(request):
    return HttpResponse('<h1>This is educationl app with application level url</h1>')