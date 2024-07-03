from django.shortcuts import render,HttpResponse
from .models import Profile
from datetime import datetime

def home_view(request):
    all_records = Profile.objects.all()
    now = datetime.now()
    d = {'all_records': all_records, 'now': now}
    return render(request, 'PropicApp/home.html', d)

def profile_details_view(request,id):
    records=Profile.objects.get(id=id)
    d={'records':records}
    return render(request,'PropicApp/profiledetails.html',d)



