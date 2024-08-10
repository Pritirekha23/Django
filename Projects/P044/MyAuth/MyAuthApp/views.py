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
            student = Student.objects.filter(email=input_email, password=input_password).first()           
            if student:
                return redirect(f'/dashboard/?email={student.email}')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = StudentsigninForm()

    return render(request, 'MyAuthApp/signin.html', {'form': form})




# def dashboard_view(request):
#     return render(request, 'MyAuthApp/dashboard.html')

def dashboard_view(request):
    student_email = request.GET.get('email')
    if student_email:
        student = Student.objects.filter(email=student_email).first()
        if student:
            context = {'student': student}
            return render(request, 'MyAuthApp/dashboard.html', context)
    return redirect('signin')