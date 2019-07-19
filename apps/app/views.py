from django.shortcuts import render, redirect
from django.contrib import messages
import re
import json
import urllib.request

urlData = "https://api.giphy.com/v1/gifs/search?api_key=Zhk5VBNNWaswfFjyy5hlik8I87lE8bgi&q=arcticmonkeys&limit=2&offset=0&rating=G&lang=en"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
jsonObject = (json.loads(data.decode('utf-8')))
print(jsonObject)

def index(request):
    return render(request, "app/index.html")

def database(request):
    return render(request, "app/database.html")

def passwordHtml(request):
    return render(request, "app/password.html")

def password(request):
    p = request.POST
    
    if request.method == 'POST':
        
        low = p['password'].lower()
        print(low)
        if low != 'dojo':
            messages.error(request, 'Not Worthy')
            return redirect('/post')
        else:
            return redirect('/add')        

def add(request):
    return render(request, "app/add.html")

