from email import message
from turtle import title
from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
# Create your views here.


def home(request):
    # allPost = Post.objects.all()
    # # print(allPost)
    # context = {'allpost':allPost}
    return render(request,'home/home.html')

def contact(request):
    # messages.success(request, 'welcome to Contact.')
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        desc = request.POST.get("desc")

        if len(name)<1 or len(email)<1 or len(phone)<10 or len(email)<5 or len(password)<8:
            messages.error(request,"Enter all Credentials")

        else:
            contact_details = Contact(name = name,phone = phone, email = email, password=password,desc =desc)
            contact_details.save()
            messages.success(request,"Contact saved Successfully...!")

        return render(request,'home/contact.html')


    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['search']

    if len(query)>78 or query=='':
        allPost = Post.objects.none()

    # if query =='HTTP/1.1':
    #      messages.warning(request,"No search result found...!")

    else:
        allPosttitle = Post.objects.filter(title__icontains=query)
        allPostcontent = Post.objects.filter(content__icontains=query)
        allPost = allPosttitle.union(allPostcontent)

    if allPost.count() == 0 :
       messages.warning(request,"No search result found...!")

    params = {'allPost':allPost,'query':query}
    
    return render (request,'home/search.html',params)


# Authentication API

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
      

        if  not username.isalnum():
            messages.warning(request, " Username must be characters and numbers only")
            return redirect('home')

        if len(username) > 10 :
            messages.warning(request, " Username should must be 10 characters only")
            return redirect('home')

        if pass1 != pass2:
            messages.warning(request, " password didn't match")
            return redirect('home')
      
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

    
def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword = request.POST['pass']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"You are successfully login...!")
            return redirect ('/')

        else:
             messages.warning(request,"invalid credential ...! Enter correct credentials..!")
             return redirect('home')

    else:
        return HttpResponse("404 - Not found")  


def handlelogout(request):
    logout(request)
    messages.success(request,"You are successfully logout....!")
    return redirect('/')



