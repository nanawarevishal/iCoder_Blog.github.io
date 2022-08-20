from django.shortcuts import render,HttpResponse
from matplotlib import blocking_input
from numpy import block
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
       
    }
    # messages.success(request,"this is test messafe")
    return render(request,'index.html',context)
    # return HttpResponse("This is vishal Home page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is vishal About page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is our services")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        contact = Contact(name = name,email = email, textarea = textarea,date = datetime.today())
        contact.save()
        messages.success(request, 'Your meassage has been sent successfully.')
    return render(request,'contact.html')
    # return HttpResponse("This is our contact")
# Create your views here.
