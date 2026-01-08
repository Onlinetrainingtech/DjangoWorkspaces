from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("welcome to the Application")
    return render(request, 'home.html')
def about(request):
    # return HttpResponse("This is the about page of the Application")
    return render(request, 'about.html')
def contact(request):
    # return HttpResponse("This is the contact page of the Application")
    return render(request, 'contact.html')
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

