from django.shortcuts import render
from datetime import datetime

def time_view(request):
    current_date_time=datetime.now()
    time=current_date_time.strftime('%H:%M:%S')
    d={'time':time}
    return render(request,'TemplateTagApp/time.html/',d)
