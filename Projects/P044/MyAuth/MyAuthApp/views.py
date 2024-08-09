from django.shortcuts import render,redirect
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
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password']
            students = Student.objects.all()
            for student in students:
                if (student.email == input_email and 
                    student.password == input_password):
                    return redirect('dashboard')             
            form.add_error(None, 'Invalid name, email, or password')
    
    else:
        form = StudentsigninForm()

    context = {'form': form}
    return render(request, 'MyAuthApp/signin.html', context)




def dashboard_view(request):
    return render(request, 'MyAuthApp/dashboard.html')