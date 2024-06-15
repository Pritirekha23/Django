from django.shortcuts import render
from .forms import Employeedetails

def employee_view(request):
    if request.method=='POST':
        #capturing form data by using dictionary get() method.
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        d={'name':name,'age':age,'email':email}
        return render(request,'FormApp/welcome.html',d)
    else:
       form=Employeedetails()
       d={'form':form}
       return render(request,'FormApp/forms.html',d)
    
