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

def edit_employee(request, id):
    # Fetches the employee record using the given id.
     #If the employee does not exist, Django automatically shows a 404 error page.
    employee = get_object_or_404(Employee, id=id)
    #Checks whether the form is submitted.
    #POST means the user clicked the Update/Submit button.
    if request.method == 'POST':
        #request.POST → data entered by the user.
        #instance=employee → tells Django to update this employee, not create a new one.
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            #Redirects to the employee list/details page after update.
            return redirect('view_detail')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'contact.html', {'form': form})

def delete_employee(request,id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('view_detail')
