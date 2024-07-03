from django.shortcuts import render


# Create your views here.
def india_view(request):
    return render(request,'countryApp/india.html')
def usa_view(request):
    return render(request,'countryApp/usa.html')
def uk_view(request):
    return render(request,'countryApp/uk.html')