from django.shortcuts import render,HttpResponse
from .forms import Employeedetails

def employee_view(request):
    if request.method=='POST':
      form=Employeedetails(request.POST)
      if form.is_valid():
        name=form.cleaned_data['name']
        age=form.cleaned_data['age']
        email=form.cleaned_data['email']
        d={'name':name,'age':age,'email':email}
        return render(request,'FormApp/welcome.html',d)
      else:
         return HttpResponse('Invalid data')
    else:
       form=Employeedetails()
       d={'form':form}
    return render(request,'FormApp/forms.html',d)



#Capture form data using dict get method
# from django.shortcuts import render,HttpResponse
# from .forms import Employeedetails

# def employee_view(request):
#     if request.method=='POST':
#       form=Employeedetails(request.POST)
#       if form.is_valid():
#            name=form.cleaned_data.get('name')
#            age=form.cleaned_data.get('age')
#            email=form.cleaned_data.get('email')
#            d={'name':name,'age':age,'email':email}
#            return render(request,'FormApp/welcome.html',d)
#       else:
#            return HttpResponse('Invalid data')
#     else:
#         form=Employeedetails()
#         d={'form':form}
#     return render(request,'FormApp/forms.html',d)

     
   
    