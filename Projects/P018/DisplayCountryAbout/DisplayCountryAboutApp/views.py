from django.shortcuts import render
from .models import Country

def home_view(request):
    all_records=Country.objects.all()
    d={'all_records':all_records}
    return render(request,'DisplayCountryABoutApp/home.html',d)

def specfic_country_record(request,id):
    records=Country.objects.get(id=id)
    d={'records':records}
    return render(request,'DisplayCountryABoutApp/description.html',d)