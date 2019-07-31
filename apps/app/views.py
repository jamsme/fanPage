from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
import re
import json
import urllib.request
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    posts = Post.objects.all().order_by("-created_at")
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    content = {
        'obj' : obj
    }

    return render(request, "app/index.html", content)

def database(request):
    posts = Post.objects.all().order_by("-created_at")

    one = Post.objects.all().order_by("-created_at").first()
    # date = one.created_at
    # gotMonth = date.strftime('%B')

    content = {
        'post' : posts
        # 'month' : gotMonth
    }
    
    return render(request, "app/database.html", content)


def passwordHtml(request):
    if not "user_id" in request.session:
        print("didn't get the password yet")
        return render(request, "app/password.html")
    else:
        return redirect('/add')

def password(request):
    p = request.POST
    
    if request.method == 'POST':

        low = p['password'].lower()
        print(low)
        if low != 'dojo':
            messages.error(request, 'Not Worthy')
            return redirect('/post')
        else:
            request.session["user_id"] = "user_id"
            request.session.set_expiry(1800)
            return redirect("/add")       

def add(request):
    if not "user_id" in request.session:
        print("didn't get the password yet")
        return redirect("/")
    
    return render(request, "app/add.html")

def submitPost(request):
    if not "user_id" in request.session:
        print("didn't get the password yet")
        return redirect("/")

    p = request.POST

    if request.method == 'POST':

        squish = p['search'].replace(" ", "+")
        print(squish)
        num = random.randint(1,200)
        print(num)
        urlData = "https://api.giphy.com/v1/gifs/search?q=" + squish + "&api_key=Zhk5VBNNWaswfFjyy5hlik8I87lE8bgi&offset=" + str(num) + "&limit=" + p['limit']
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        jsonObject = (json.loads(data.decode('utf-8')))

        content = {
            'search' : jsonObject
        }


    return render(request, "app/add.html", content)

def append(request):
    p = request.POST
    
    if request.method == 'POST':

        check = Post.objects.all()
        gotUrl = p['url'].split("/")
        # print(gotUrl[4])

        for q, val in enumerate(check):
            res = val.__dict__['url']
            splitDatabase = res.split("/")
            # print("DATABASE ========== ",q,splitDatabase[4])
            if splitDatabase[4] == gotUrl[4]:
                print("Already have it",splitDatabase[4],"=",gotUrl[4])
                messages.error(request, 'Already have that one')
                return redirect("/add")

        
        print(p["title"])
        remove = p["title"].replace("GIF", "")
        uppercase = remove.title()
        Post.objects.create(url=p["url"], title=uppercase)
        Post.objects.order_by("created_at")

    return redirect("/")

def delete(request, post_id):
    bye = Post.objects.get(id=post_id)
    print("delete")
    print(bye)
    bye.delete()

    return redirect("/database")



