from django.shortcuts import render
from .forms import Employeedetails

def employee_view(request):
    if request.method=='POST':
        #capture the form data
        form=Employeedetails(request.POST)
        d={'form':form}
        return render(request,'FormApp/welcome.html',d)
    else:
       form=Employeedetails()
       d={'form':form}
       return render(request,'FormApp/forms.html',d)
