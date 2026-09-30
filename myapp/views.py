from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'register.html', {'error_message': error_message})
        
        # Create a new user
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save() 
        return redirect('login')  # Redirect to the login page after successful registration
        

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page after successful login
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def dashboard(request):
    return render(request, 'dashboard.html')