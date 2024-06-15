from django.shortcuts import render
from .forms import Studentform

def Student_view(request):
    form=Studentform()
    d={'form':form}
    return render(request,'FormApp2/forms.html',d)