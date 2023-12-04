from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Category,Post,Save
from django.db.models import Q

# Create your views here.

def home(request):
    #userid= request.user.id
    #print(userid)
    c=Category.objects.filter(is_active=True)
    p=Post.objects.filter(is_active=True)

    context={}
    context['categories']=c
    context['posts']=p
    #print("result :",request.user.is_authenticated)
    return render(request,'index.html',context)

def about(request):
    c=Category.objects.filter(is_active=True)
    p=Post.objects.filter(is_active=True)

    context={}
    context['categories']=c
    context['posts']=p
    return render(request,'about.html',context)

def contact(request):
    c=Category.objects.filter(is_active=True)
    p=Post.objects.filter(is_active=True)

    context={}
    context['categories']=c
    context['posts']=p
    
    return render(request,'contact.html',context)

def catfilter(request,cat_id):
    
    c=Category.objects.filter(is_active=True)
    p=Post.objects.filter(cat_id=cat_id)
    #print(p)
    #print(c)
    context={}
    context['posts']=p
    #context['categories']=c
    return render(request,'index.html',context)

def register(request):
    
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Fields can not be empty"
            return render(request,'register.html',context)
        elif upass != ucpass:
            context['errmsg']="password and confirm password didn't match"
            return render(request,'register.html',context)
        else:
            try:
                #print(uname,"-",upass,"-",ucpass)
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context['success']="User created Successfully"
                return render(request,'register.html',context)
                #return HttpResponse("Data is fetched")
            except:
                context['errmsg']="User with same username alresdy exist"
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        #return render(request,'index.html')
        context={}
        if uname=="" or upass=="":
            context['errmsg']="fields can not be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['errmsg']="Invalid username and password"
                return render(request,'login.html',context)

    else:
        return render(request,'login.html')

def header(request):
    
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def post(request):
    c=Category.objects.filter(is_active=True)
    p=Post.objects.filter(is_active=True)

    context={}
    context['categories']=c
    #context['posts']=p
    #p=Post.objects.all()
    #c=Category.objects.filter(cat_id=cat_id)

    #print(c)
    context={}
    context['posts']=p
    
    return render(request,'post.html',context)
        

def readpost(request,cat_id):

    #q1=Q(is_active=True)
    #q2=Q(title=pv)
    p=Post.objects.filter(cat_id=cat_id)
    #print(p)
    c=Category.objects.filter(cat_id=cat_id)

    #print(c)
    context={}
    context['posts']=p
    
    return render(request,'index.html',context)
    
def save(request,pid):

    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        p=Post.objects.filter(post_id=pid)
        q1=Q(uid=u[0])
        q2=Q(pid=p[0])
        s=Save.objects.filter(q1 & q2)
        n=len(s)
        print(n)
        context={}
        context['posts']=p
        if n==1:
            context['msg']="Post is already saved"
        else:
            s=Save.objects.create(uid=u[0],pid=p[0])
            s.save()
            
            context['success']="Post is successfuly saved"
        return render(request,'post.html',context)
        #return HttpResponse("successfully save")
    else:
        return redirect('/login')

def viewsaved(request):
    c=Category.objects.filter(is_active=True)
    p=Post.objects.filter(is_active=True)
    
    s=Save.objects.filter(uid=request.user.id)
    context={}
    context['data']=s
    context['categories']=c
    context['posts']=p
    return render(request,'save.html',context)

def remove(request,pid):
    p=Save.objects.filter(id=pid)
    p.delete()
    return redirect('/viewsaved')


def user_logout(request):
    logout(request)
    return redirect('/home')



