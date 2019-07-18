from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, "app/index.html")

def database(request):
    return render(request, "app/database.html")

def passwordHtml(request):
    return render(request, "app/password.html")

def password(request):
    p = request.POST

    if request.method == 'POST':

        if p['password'] != 'Alex':
            return redirect('/')
        else:
            return redirect('/add')        

def add(request):
    return render(request, "app/add.html")

