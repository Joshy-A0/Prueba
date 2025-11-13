from django.shortcuts import render

def login(request):
    return render(request, 'miapp/login.html')

def control(request):
    return render(request, 'miapp/ManoRobotica.html')
