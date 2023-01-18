from django.shortcuts import render,redirect
from server.apps.posts.models import Idea,Devtool
from django.http.request import HttpRequest

# Create your views here.

def ideas_create(request:HttpRequest,*args, **kwargs):
    tools=Devtool.objects.all().values_list("name",flat=True)
    
    context={
        "tools":tools,
    }
    
    if request.method=="POST":
        tool_name=request.POST["tool"]
        dtool=Devtool.objects.get(name=tool_name)#Devtool instance로 전달해주기 위해변환
            
        Idea.objects.create(
            title=request.POST["title"],
            image=request.FILES.get("image"),
            content=request.POST["content"],
            interest=request.POST["interest"],
            tool=dtool,
        )
        
        return redirect("/")
    return render(request,"posts/ideas_create.html",context=context)

def ideas_list(request:HttpRequest,*args, **kwargs):
    posts=Idea.objects.all()
    
    context={
        "posts":posts,
    }
    
    return render(request,"posts/ideas_list.html",context=context)

def ideas_retrieve(request:HttpRequest,pk,*args, **kwargs):
    post=Idea.objects.get(id=pk)
    selected_tool=Devtool.objects.get(name=post.tool.name)

    context={
        "post":post,
        "selected_tool":selected_tool,
    }
    
    
    return render(request,"posts/ideas_retrieve.html",context=context)

def ideas_delete(request:HttpRequest,pk,*args, **kwargs):
    if request.method=="POST":
        post=Idea.objects.get(id=pk)
        post.delete()
    return redirect("/")

def ideas_update(request:HttpRequest,pk,*args, **kwargs):
    post=Idea.objects.get(id=pk)
    
    tools=Devtool.objects.all().values_list("name",flat=True)
   
    context={
        "post":post,
        "tools":tools,
    }
    
    if request.method=="POST":
        tool_name=request.POST["tool"]
        dtool=Devtool.objects.get(name=tool_name)#Devtool instance로 전달해주기 위해변환
        
        post.title=request.POST["title"]
        post.image=request.FILES.get("image")
        post.content=request.POST["content"]
        post.interest=request.POST["interest"]
        post.tool=dtool
        
        post.save()
        
        return redirect("/ideas/{}".format(post.id))
    return render(request,"posts/ideas_update.html",context=context)
    
#devtool
def devtool_list(request:HttpRequest,*args, **kwargs):
    posts=Devtool.objects.all()
    
    context={
        "posts":posts,
    }
    
    return render(request,"posts/devtool_list.html",context=context)

def devtool_create(request:HttpRequest,*args, **kwargs):
    if request.method=="POST":
        Devtool.objects.create(
            name=request.POST["name"],
            content=request.POST["content"],
            kind=request.POST["kind"],
        )
        
        return redirect("/devtool/list")
    return render(request,"posts/devtool_create.html")
        
def devtool_retrieve(request:HttpRequest,pk,*args, **kwargs):
    post=Devtool.objects.get(id=pk)
    
    # 기능 12...
    # idea=Idea.objects.filter(tool=post.name)
    # idea_tool=idea.tool
    # all_ideas=idea_tool.used_tool.all()
    
    context={
        "post":post,
        #"all_ideas":all_ideas,
    
    }
    return render(request,"posts/devtool_retrieve.html",context=context)

def devtool_delete(request:HttpRequest,pk,*args, **kwargs):
    if request.method=="POST":
        post=Devtool.objects.get(id=pk)
        post.delete()
    return redirect("/devtool/list")

def devtool_update(request:HttpRequest,pk,*args, **kwargs):
    post=Devtool.objects.get(id=pk)
    context={
        "post":post,
    }
    
    if request.method=="POST":
        post.name=request.POST["name"]
        post.content=request.POST["content"]
        post.kind=request.POST["kind"]
        
        post.save()
        
        return redirect("/devtool/{}".format(post.id))
    return render(request,"posts/devtool_update.html",context=context)
    
    