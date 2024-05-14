from django.shortcuts import render

# Create your views here.
def odisha_view(request):
    return render(request,'TemplateApp/odisha.html')