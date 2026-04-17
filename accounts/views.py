from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

def login(request):
    # check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not username:
            messages.error(request, "Username is required")
            return render(request, 'accounts/login.html')
        
        if not password:
            messages.error(request, "Password is required")
            return render(request, "accounts/login.html")
        
        # authenticate the user
        user = authenticate(request, username = username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')
   

def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST': #if the request is POST
        # create the form with POST data
        form = CreateUserForm(request.POST)
        # if the form is valid
        if form.is_valid():
            # save the user
            user = form.save()
            # success message
            messages.success(request, f'Account created successfully for {user.username}, you can now login!')
            # return to the login page
            return redirect('login')

        else:
            messages.error(request, "Please correct the errors below ")    
    
    # if it is GET request, create an empty form
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form' : form})

@login_required(login_url = 'login')
def dashboard(request):
    user = request.user
    tasks = user.task_set.all()
    tags = user.tag_set.all()
    return render(request, 'pages/dashboard.html', {
        'tasks' : tasks,
        'tags':tags
    })
