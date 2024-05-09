from django.shortcuts import render,HttpResponse

# Create your views here.
def cricket_view(request):
    return HttpResponse('<h2>This is cricket app</h2>')
