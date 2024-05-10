from django.shortcuts import render,HttpResponse

# Create your views here.
def wish_view(req):
    return HttpResponse("Hello Good morning Priti")