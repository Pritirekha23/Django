from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

def set_cookie_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            res = HttpResponse("Cookie is set")
            res.set_cookie('name', name)
            return res
    else:
        form = NameForm()
    return render(request, 'CookieApp/set_cookie.html', {'form': form})

def get_cookie_view(request):
    name=request.COOKIES['name']
    res=HttpResponse('Cookie name is ' +name)
    return res

def delete_cookie_view(request):
    res=HttpResponse("Cookie is deleted")
    res.delete_cookie('name')
    return res

