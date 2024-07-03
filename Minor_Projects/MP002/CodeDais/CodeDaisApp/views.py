from django.shortcuts import render
from .models import Course,Trainers,Enquire,Testimonials
from .forms import Enquireform

# Create your views here.
def home_view(request):
    return render(request,'CodeDaisApp/home.html')

def courses_view(request):
    all_courses=Course.objects.all()
    context={'all_courses':all_courses}
    return render(request,'CodeDaisApp/courses.html',context)

def trainers_view(request):
    all_trainers=Trainers.objects.all()
    all_testimonials=Testimonials.objects.all()
    context={'all_trainers':all_trainers,'all_testimonials':all_testimonials}
    return render(request,'CodeDaisApp/trainers.html',context)

def blogs_view(request):
    return render(request,'CodeDaisApp/blogs.html')

def aboutus_view(request):
    return render(request,'CodeDaisApp/aboutus.html')

def contactus_view(request):
    form_submitted = False  
    if request.method == 'POST':
        form = Enquireform(request.POST)
        if form.is_valid():
            form.save()
            form_submitted = True 
            form = Enquireform()  
    else:
        form = Enquireform()
    
    context = {'form': form, 'form_submitted': form_submitted}
    return render(request, 'CodeDaisApp/contactus.html', context)


