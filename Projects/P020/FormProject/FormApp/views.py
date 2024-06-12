from django.shortcuts import render
from .forms import Student_form

def form_view(request):
    form=Student_form()
    d={'form':form}
    return render(request,'FormApp/home.html',d)
