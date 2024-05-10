from django.shortcuts import render,HttpResponse


def politics_view(request):
    return HttpResponse('<h2>This is Politics app with application level url</h2>')
