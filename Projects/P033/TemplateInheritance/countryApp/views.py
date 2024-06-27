from django.shortcuts import render
from .models import Indiaplaces,Usaplaces,Ukplaces

# Create your views here.
def india_view(request):
    all_records=Indiaplaces.objects.all()
    context={'all_records':all_records}
    return render(request,'countryApp/india.html',context)
def usa_view(request):
    all_records=Usaplaces.objects.all()
    context={'all_records':all_records}
    return render(request,'countryApp/usa.html',context)
def uk_view(request):
    all_records=Ukplaces.objects.all()
    context={'all_records':all_records}
    return render(request,'countryApp/uk.html',context)