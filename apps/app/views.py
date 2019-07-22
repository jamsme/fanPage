from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
import re
import json
import urllib.request

def index(request):
    posts = Post.objects.all().order_by("-created_at")

    content = {
        'post' : posts
    }

    return render(request, "app/index.html", content)

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

def submitPost(request):
    p = request.POST

    if request.method == 'POST':

        squish = p['search'].replace(" ", "+")
        print(squish)
        urlData = "https://api.giphy.com/v1/gifs/search?q=" + squish + "&api_key=Zhk5VBNNWaswfFjyy5hlik8I87lE8bgi&limit=" + p['limit']
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        jsonObject = (json.loads(data.decode('utf-8')))

        content = {
            'search' : jsonObject
        }
        # print(json.dumps(jsonObject, sort_keys=True, indent=4))

    return render(request, "app/add.html", content)

def append(request):
    p = request.POST
    
    if request.method == 'POST':
        
        Post.objects.create(url=p["url"])
        Post.objects.order_by("created_at")

    return redirect("/")

def delete(request, post_id):
    bye = Post.objects.get(id=post_id)
    print("delete")
    print(bye)
    bye.delete()

    return redirect("/")



