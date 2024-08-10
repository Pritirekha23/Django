from django.shortcuts import render,HttpResponse

def session_view(request):
    request.session['name']='surendra'
    request.session['email']='example@gmail.com'
    request.session['mark']=78
    return HttpResponse('Session is set')

def get_session_view(request):
    name=request.session['name']
    email=request.session['email']
    mark=request.session['mark']
    items=request.session.items()
    keys=request.session.keys()
    exp_date=request.session.get_expiry_date()
    exp_age=request.session.get_expiry_age()
    context={
        'name':name,
        'email':email,
        'mark':mark,
        'items':items,
        'keys':keys,
        'exp_date':exp_date,
        'exp_age':exp_age,
    }
    return render(request,'SessionApp/get_session.html',context)


    
def delete_session_view(request):
    del request.session['mark']
    return HttpResponse('In Session  mark is  deleted')
    

def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    c=request.session['count']=newcount
    return HttpResponse(c)
