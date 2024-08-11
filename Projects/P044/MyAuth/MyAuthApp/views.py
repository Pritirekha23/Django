from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentForm,StudentsigninForm
from .models import Student


def home_view(request):
    return render(request, 'MyAuthApp/home.html')


def signup_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success')  
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, 'MyAuthApp/signup.html', context)


def success_view(request):
    return render(request, 'MyAuthApp/success.html')




def signin_view(request):
    if request.method == "POST":
        form = StudentsigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            students = Student.objects.filter(email=email)
            
            if students.exists():
                student = students.first()                 
                if student.password == password:
                    context = {'student': student}
                    return render(request, 'MyAuthApp/dashboard.html', context)
                else:
                    return HttpResponse("wrong email or password")
            else:
                return HttpResponse("wrong email or password")
    else:
        form = StudentsigninForm()

    return render(request, 'MyAuthApp/signin.html', {'form': form})



def dashboard_view(request):
    student_email = request.GET.get('email')
    if student_email:
        student = Student.objects.filter(email=student_email).first()
        if student:
            context = {'student': student}
            return render(request, 'MyAuthApp/dashboard.html', context)
    return redirect('signin')