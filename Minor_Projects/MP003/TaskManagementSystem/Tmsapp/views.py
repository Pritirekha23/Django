from django.shortcuts import render,redirect,get_object_or_404
from .models import TaskDetails

def home_view(request):
    incomplete_task=TaskDetails.objects.filter(task_status=False)
    complete_task=TaskDetails.objects.filter(task_status=True)
    len_incomplete_task=len(incomplete_task)
    len_complete_task=len(complete_task)
    total_no_task=TaskDetails.objects.all().count()
    if total_no_task > 0:
        percent_complete_task = (len_complete_task / total_no_task) * 100
    else:
        percent_complete_task = 0

    context={
        'incomplete_task':incomplete_task,
        'complete_task':complete_task,
        'len_incomplete_task':len_incomplete_task,
        'len_complete_task':len_complete_task,
        'total_no_task':total_no_task,
        'total_no_complete_task':len(complete_task),
        'total_no_incomplete_task':len(incomplete_task),
        'percent_complete_task':int(percent_complete_task)

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


def done_all_view(request):
    TaskDetails.objects.all().update(task_status=True)
    return redirect('home')


def undo_task_view(request,id):
    record=get_object_or_404(TaskDetails,id=id)
    record.task_status=False
    record.save()
    return redirect('home')

def undo_all_view(request):
    TaskDetails.objects.all().update(task_status=False)
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

def  update_task_view(request,id):
    if request.method=='POST':
        update_task=request.POST['update_task']
        record=get_object_or_404(TaskDetails,id=id)
        record.task_name=update_task
        record.save()
        return redirect('home')
    else:
        record=get_object_or_404(TaskDetails,id=id)
        task_name=record.task_name
        id=record.id
        context={
            'task_name':task_name,
            'id':id,
        }
        return render(request,'Tmsapp/update.html',context)