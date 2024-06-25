from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def student_view(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        data_valid=False
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            adhar_number=form.cleaned_data['adhar_number']
            address=form.cleaned_data['address']
            upload_cv=form.cleaned_data['upload_cv']
            password=form.cleaned_data['password']
            data_valid=True
            d={'data_valid':data_valid}          
            return render(request,'FormValidationsApp/success.html',d)
        else:
            d={'form':form}
            return render(request,'FormValidationsApp/success.html',d)     
    else:
        form=StudentForm()
        d={'form':form}
        return render(request,'FormValidationsApp/form.html',d)
