from django.shortcuts import render,HttpResponse

def education_form_view(request):
    return render(request,'StudentInfoApp/education_form.html')
def personal_form_view(request):
    college=request.GET['college']
    degree=request.GET['degree']
    mark=request.GET['mark']
    response=render(request,'StudentInfoApp/personal_form.html')
    response.set_cookie('college',college)
    response.set_cookie('degree',degree)
    response.set_cookie('mark',mark)
    return response
def extra_cur_form_view(request):
    name=request.GET['name']
    address=request.GET['address']
    email=request.GET['email']
    response=render(request,'StudentInfoApp/extra_cur.html')
    response.set_cookie('name',name)
    response.set_cookie('address',address)   
    response.set_cookie('email',email)
    return response
from django.shortcuts import render,HttpResponse

def education_form_view(request):
    return render(request,'StudentInfoApp/education_form.html')
def personal_form_view(request):
    college=request.GET['college']
    degree=request.GET['degree']
    mark=request.GET['mark']
    response=render(request,'StudentInfoApp/personal_form.html')
    response.set_cookie('college',college)
    response.set_cookie('degree',degree)
    response.set_cookie('mark',mark)
    return response
def extra_cur_form_view(request):
    name=request.GET['name']
    address=request.GET['address']
    email=request.GET['email']
    response=render(request,'StudentInfoApp/extra_cur.html')
    response.set_cookie('name',name)
    response.set_cookie('address',address)   
    response.set_cookie('email',email)
    return response
def data_view(request):
    fav_sports = request.GET['fav_sports']
    fav_actor = request.GET['fav_actor']
    context = {
        'all_records': request.COOKIES
    }
    response = render(request, 'StudentInfoApp/data.html', context)
    response.set_cookie('fav_sports', fav_sports)
    response.set_cookie('fav_actor', fav_actor)
    
    return response