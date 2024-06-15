from django.shortcuts import render
from .forms import StudentForm

def Student_form_view(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            if password==confirm_password:
                d={'matched':True}
                return render(request,'FormFieldApp/welcome.html',d)
            else:
                d={'matched':False}
                return render(request,'FormFieldApp/welcome.html',d)
            
    form=StudentForm()
    d={'form':form}
    return render(request,'FormFieldApp/form.html',d)

