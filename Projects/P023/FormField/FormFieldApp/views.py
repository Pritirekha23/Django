from django.shortcuts import render
from .forms import StudentForm

def Student_form_view(request):
    form=StudentForm()
    d={'form':form}
    return render(request,'FormFieldApp/form.html',d)

