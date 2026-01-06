from django.shortcuts import render
from django.http import HttpResponse

def department_home(request):
    return HttpResponse("Welcome to the Department Home Page")
