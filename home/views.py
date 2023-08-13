from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, logout
from home.models import Booking
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def booking(request):
    if request.method =="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phnumber=request.POST.get('phnumber')
        startdate=request.POST.get('startdate')
        finishdate=request.POST.get('finishdate')
        country=request.POST.get('country')
        subject=request.POST.get('subject')
        book=Booking(firstname=firstname, lastname=lastname, email=email, phnumber=phnumber, startdate=startdate, finishdate=finishdate, country=country, subject=subject)
        book.save()
        messages.success(request,"we will contect you soon..")
    return render(request,'booking.html')

def gallery(request):
    return render(request, 'gallery.html')

def kolkata(request):
    return render(request, 'kolkata.html')

def jaipur(request):
    return render(request, 'jaipur.html')

def login(request):
    # UserName : akarmakar891@gmail.com
    # Password : Arindam2*
    if request.method =="POST":
        username=request.POST.get('uname')
        password=request.POST.get('psw')
        user = authenticate(username=username, password=password)
        if user is not None:
            blog =Booking.objects.all().values('country')
            # template=loader.get_template('admin_details.html')
            context={
                'blog':blog
            }
            return render(request, 'admin_details.html', context)
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def admin(request):
    if request.user.is_anonymous:
        return redirect('login')
    blog =Booking.objects.all().values('country')
    # template=loader.get_template('admin_details.html')
    context={
        'blog':blog
    }
    return render(request, 'admin_details.html', context)

def logoutuser(request):
    logout(request)
    return render(request, 'login.html')

def details_user(request,country):
    detl= Booking.objects.all().values().filter(country=country)
    # temp=loader.get_template('d1.html')
    context={
        'detl':detl
    }
    # return HttpResponse(temp,render(context,request))
    return render(request, 'details.html', context)
    # return HttpResponse("I am in details")