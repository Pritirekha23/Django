from django.shortcuts import render,HttpResponse

def politics_view(request):
    return HttpResponse('<h3>This is politics app</h3>')
