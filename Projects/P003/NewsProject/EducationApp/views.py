from django.shortcuts import render,HttpResponse

# Create your views here.
def education_view(request):
    return HttpResponse('<h1>This is educationl app</h1>')