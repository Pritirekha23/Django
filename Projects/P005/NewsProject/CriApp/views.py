from django.shortcuts import render,HttpResponse


def cricket_view(request):
    return HttpResponse('<h1>This is cricket app with application level url</h1>')