from django.shortcuts import render, redirect, get_object_or_404

# importing models
from .models import Task

# importing forms
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'ToDo/task_list.html', {'tasks' : tasks})

def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(task_list)

    return render(request, 'ToDo/add_task.html', {'form' : form}) 

def complete_task(request, task_id):
    # first retrieve the data from the database
    task = get_object_or_404(Task, pk=task_id)
    # then complete the task
    task.completed = True
    # the save the task
    task.save()
    # return redirect('task_list')
    return render (request, 'ToDo/complete_task.html', {'task': task}) 
 
def delete_task(request, task_id):
    # first retrieve the data from the database
    task = get_object_or_404(Task, pk=task_id)
    # checking if the request is POSt
    if request.method == 'POST':
        # delete the task
        task.delete()
        return redirect('task_list')
    return render(request, 'ToDo/delete_task.html', {'task':task})