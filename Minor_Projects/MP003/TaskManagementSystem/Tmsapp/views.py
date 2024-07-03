from django.shortcuts import render,redirect,get_object_or_404
from .models import TaskDetails

def home_view(request):
    incomplete_task=TaskDetails.objects.filter(task_status=False)
    complete_task=TaskDetails.objects.filter(task_status=True)
    len_incomplete_task=len(incomplete_task)
    len_complete_task=len(complete_task)
    context={
        'incomplete_task':incomplete_task,
        'complete_task':complete_task,
        'len_incomplete_task':len_incomplete_task,
        'len_complete_task':len_complete_task
    }
    return render(request,'Tmsapp/home.html',context)


def add_task_view(request):
    task_add=request.POST['addtask']
    TaskDetails.objects.create(task_name=task_add)
    return redirect('home')


def done_task_view(request,id):
    record=get_object_or_404(TaskDetails,id=id)
    record.task_status=True
    record.save()
    return redirect('home')

def undo_task_view(request,id):
    record=get_object_or_404(TaskDetails,id=id)
    record.task_status=False
    record.save()
    return redirect('home')

def delete_task_view(request,id):
    record=get_object_or_404(TaskDetails,id=id)
    record.delete()
    return redirect('home')

def delete_all_view(request):
    incomplete_task=TaskDetails.objects.filter(task_status=False)
    incomplete_task.delete()
    return redirect('home')

def clear_all_view(request):
    completed_task=TaskDetails.objects.filter(task_status=True)
    completed_task.delete()
    return redirect('home')

def remove_all_view(request):
    all_records=TaskDetails.objects.all()
    all_records.delete()
    return redirect('home')