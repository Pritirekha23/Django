from django.shortcuts import render
from .models import Profile

def home_view(request):
    all_records=Profile.objects.all()
    d={'all_records':all_records}
    return render(request,'PropicApp/home.html',d)

def profile_details_view(request,id):
    records=Profile.objects.get(id=id)
    d={'records':records}
    return render(request,'PropicApp/profiledetails.html',d)