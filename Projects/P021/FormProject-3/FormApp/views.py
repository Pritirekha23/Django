from django.shortcuts import render
from .forms import Employeedetails

def employee_view(request):
    form=Employeedetails()
    d={'form':form}
    return render(request,'FormApp/forms.html',d)

def employee_process_view(request):
        #capture data by using HTTP GET request 
        name=request.GET['name']
        age=request.GET['age']
        email=request.GET['email']
        d={'name':name,'age':age,'email':email}
        return render(request,'FormApp/welcome.html',d)


# def employee_process_view(request):
#         #capture data by using dict get method 
#         name=request.GET.get('name')
#         age=request.GET.get('age')
#         email=request.GET.get('email')
#         d={'name':name,'age':age, 'email':email}
#         return render(request,'FormApp/welcome.html',d)

    
