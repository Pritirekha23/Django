from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RedgForm
# Create your views here.
def redg_view(request):
    if request.method=='POST':
        form=RedgForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registraction Successful')
    form=RedgForm()
    return render(request,'Signin_SignupApp/form.html',{'form':form})

def signin_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user!=None:
                login(request,user)
                return HttpResponseRedirect('/Signin_SignupApp/dashboard/')
    elif request.user.is_authenticated:
        return HttpResponseRedirect('/Signin_SignupApp/dashboard/')
    else:    
        form=AuthenticationForm()
    return render(request,'Signin_SignupApp/Signin.html',{'form':form})

def dashboard_view(request):
    if request.user.is_authenticated:
        username=request.user
        d={'username':username}
        return render(request,'Signin_SignupApp/dashboard.html',d)
    else:
        return HttpResponseRedirect('/Signin_SignupApp/signin/')
    
def signout_view(request):
    logout(request)
    return HttpResponseRedirect('/Signin_SignupApp/signin/')
