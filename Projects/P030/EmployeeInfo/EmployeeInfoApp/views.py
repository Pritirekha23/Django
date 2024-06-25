from django.shortcuts import render,HttpResponse
from .forms import EmployeeForm
from .models import Employee

def employee_view(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            desg=form.cleaned_data['desg']
            sal=form.cleaned_data['sal']
            address=form.cleaned_data['address']
            emp=Employee(name=name,age=age,desg=desg,sal=sal,address=address)  
            emp.save()  
            context={'name':name}
            return render(request,'EmployeeInfoApp/success.html',context)
            # return HttpResponse('one record inserted successfully') 
           
    else:
        form=EmployeeForm()
        context={'form':form}
    return render(request,'EmployeeInfoApp/form.html',context)


def display_records(request):
    all_records=Employee.objects.all()
    context={'all_records':all_records}
    return render(request,'EmployeeInfoApp/display.html',context)


   