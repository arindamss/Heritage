from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, logout
from home.models import Booking

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
            blog =Booking.objects.all().values()
            template=loader.get_template('admin.html')
            context={
                'blog':blog,
            }
            return HttpResponse(template.render(context,request))
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def admin(request):
    if request.user.is_anonymous:
        return redirect('login')
    blog =Booking.objects.all().values()
    template=loader.get_template('admin.html')
    context={
        'blog':blog,
    }
    return HttpResponse(template.render(context,request))

def logoutuser(request):
    logout(request)
    return render(request, 'login.html')


# This change is made by Practice