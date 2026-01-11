from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import EmployeeForm
from .models import Employee

def home(request):
    # return HttpResponse("welcome to the Application")
    return render(request, 'home.html')
def about(request):
    # return HttpResponse("This is the about page of the Application")
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form=EmployeeForm()
    return render(request, 'contact.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically authenticate the user
        if username == 'admin' and password == 'password':
            return HttpResponse("Login successful!")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def register_view(request):
    return render(request, 'register.html')
def view_detail(request):
    employees = Employee.objects.all()
    return render(request, 'viewdetail.html', {'employees': employees})

