from django.shortcuts import render, redirect, get_object_or_404 #importing render that sends the HTML files to the browser and redirect that sends the user to the another URL
from .forms import ContactForm, TaskForm, TagForm #importing forms
from .models import Task, Tag #importing Task model
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
def add_tasks(request):
    if request.method == "POST": #user submits the form
        #create form with submitted data
        form = TaskForm(request.POST) 
        form.instance.user = request.user
        if form.is_valid(): #django checks the form
            task = form.save() #it is inserted into the database
            return redirect('dashboard') #if it is valid it sends the user to the homepage
    else: #if request.method is GET it will create a blank Taskform
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})
        
def contact_us_02(request):
    if request.method == 'POST': #if the form is submitted it create a form with the submitted data 
        form = ContactForm(data=request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            messages = form.cleaned_data['message']
            email = form.cleaned_data['email'] 

            print(f"Contact: {subject} - {messages} - {email}")
            messages.success(request, "Message sent!")
            return redirect('index')
    else: #if the request is GET request it will create an empty form and send the user back to the page
        form = ContactForm()
    return render(request, 'pages/contact_us_02.html', {'form' : form})
    

@login_required(login_url = 'login')
def add_tags(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect('dashboard')
    
    else:
        form = TagForm()

    tags = Tag.objects.all()
    return render(request, 'task/add_tags.html',{
        'form': form,
        'tags' : tags 
    })

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

@login_required(login_url='login')
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id, user=request.user)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, "Tag deleted successfully!")
        return redirect('dashboard')
    
    return redirect('add_tags')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user = request.user)
    task.status = Task.TaskStatus.COMPLETED
    task.completed_at = timezone.now()
    task.save()
    return redirect('dashboard')

@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method=='POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('dashboard')
    