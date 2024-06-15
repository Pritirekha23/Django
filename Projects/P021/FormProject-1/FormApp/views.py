from django.shortcuts import render
from .forms import Employeedetails

def employee_view(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        d={'name':name,'age':age,'email':email}
        return render(request,'FormApp/welcome.html',d)
    else:
       form=Employeedetails()
       d={'form':form}
       return render(request,'FormApp/forms.html',d)
