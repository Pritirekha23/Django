from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume

def info(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('all_resume_view')  
    else:
        form = ResumeForm()
    
    context = {'form': form}
    return render(request, 'ORBApp/info.html', context)


def all_resume_view(request):
    data = Resume.objects.all()
    context = {'data': data}
    return render(request, 'ORBApp/view.html', context)

def resume_view(request,id):
    data =get_object_or_404(Resume,id=id)
    context = {'data': data }
    return render(request, 'ORBApp/resume.html', context)



# def personal_info_view(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_summary')
#     else:
#         form = ResumeForm()
#     context = {'form': form}
#     return render(request, 'ORBApp/personal_info.html', context)

# def profile_summary_view(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('experience')
#     else:
#         form = ResumeForm()
#     context = {'form': form}
#     return render(request, 'ORBApp/profile_summary.html', context)

# def experience_view(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('education')
#     else:
#         form = ResumeForm()
#     context = {'form': form}
#     return render(request, 'ORBApp/experience.html', context)

# def education_view(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('skills_languages')
#     else:
#         form = ResumeForm()
#     context = {'form': form}
#     return render(request, 'ORBApp/education.html', context)

# def skills_languages_view(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'ORBApp/view.html')
#         else:
#             print(form.errors) 
#     else:
#         form = ResumeForm()
    
#     context = {'form': form}
#     return render(request, 'ORBApp/skills_languages.html', context)