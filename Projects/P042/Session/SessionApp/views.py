from django.shortcuts import render,HttpResponse

def session_view(request):
    request.session['name']='surendra'
    request.session['email']='example@gmail.com'
    return HttpResponse('Session is set')
    