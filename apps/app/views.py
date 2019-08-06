from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
import re
import json
import urllib.request
import random
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all().order_by("-created_at")
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)

    obj = paginator.page(page)

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

    if request.method == 'POST' and 'limit' in request.POST:

        squish = p['search'].replace(" ", "+")
        print(squish)
        num = random.randint(1,200)
        print(num)
        urlData = "https://api.giphy.com/v1/gifs/search?q=" + squish + "&api_key=Zhk5VBNNWaswfFjyy5hlik8I87lE8bgi&offset=" + str(num) + "&limit=" + p['limit']
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        jsonObject = (json.loads(data.decode('utf-8')))
        # print(json.dumps(jsonObject, indent=4, sort_keys=True))

        content = {
            'search' : jsonObject
        }

        return render(request, "app/add.html", content)

def append(request):
    p = request.POST
    
    if request.method == 'POST':

        check = Post.objects.all()
        gotUrl = p['url'].split("/")

        for q, val in enumerate(check):
            res = val.__dict__['url']
            splitDatabase = res.split("/")
            # print("DATABASE ========== ",q,splitDatabase)

            try:
                splitDatabase.index(gotUrl[4])
                messages.error(request, 'Already have that one')
                print(":( Already have it")
                return redirect("/add")
            except ValueError:
                print(":)")
            
        print("added", p["url"])
        remove = p["title"].replace("GIF", "")
        uppercase = remove.title()
        Post.objects.create(url=p["url"], title=uppercase)
        Post.objects.order_by("created_at")
        return redirect("/")

def pinterest(request):
    if not "user_id" in request.session:
        print("didn't get the password yet")
        return redirect("/")

    p = request.POST

    if request.method == 'POST' and "limit" in request.POST:

        user = "crispherr"
        board = "arctic-monkeys"
        limit = p['limit']
        print(limit)

        if limit == "":
            limit = 25

        print(limit)
        urlData = "https://api.pinterest.com/v1/boards/" + user + "/" + board + "/pins/?access_token=AhsnUXwB2Af-ni4bS7OJoYnuKv6LFbau0T6pxb9GCvTzxADPaAbbgDAAANMJRgr6GlQAy3QAAAAA&fields=image,note&limit=" + str(limit)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        jsonObject = (json.loads(data.decode('utf-8')))
        # print(json.dumps(jsonObject, indent=4, sort_keys=True))

        content = {
            'pinData' : jsonObject
        }
            
        return render(request, "app/add.html", content)

    elif request.method == 'POST' and 'extra' in request.POST:

        webURL = urllib.request.urlopen(p['extra'])
        data = webURL.read()
        jsonObject = (json.loads(data.decode('utf-8')))
        # print(json.dumps(jsonObject, indent=4, sort_keys=True))

        content = {
            'pinData' : jsonObject
        }
            
        return render(request, "app/add.html", content)

def pinterestForm(request):
    p = request.POST

    if request.method == 'POST':

        check = Post.objects.all()
        gotUrl = p['url'].split("/")
    
        for q, val in enumerate(check):
            res = val.__dict__['url']
            splitDatabase = res.split("/")
            # print("DATABASE ========== ",q,splitDatabase)

            try:
                splitDatabase.index(gotUrl[7])
                messages.error(request, 'Already have that one')
                print(":( Already have it")
                return redirect("/add")
            except:
                print(":)")       
        
        Post.objects.create(url=p["url"], title=p["title"])
        Post.objects.order_by("created_at")
        print("added ", p['title'], " + ", p['url'])
        return redirect("/")        

def delete(request, post_id):
    bye = Post.objects.get(id=post_id)
    print("delete")
    print(bye.url)
    bye.delete()

    return redirect("/database")



