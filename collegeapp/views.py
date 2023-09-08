from django.contrib import messages, auth
from django.contrib.auth.models import User, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404



def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
          user = User.objects.create_user(username=username,password=cpassword)

          user.save();
          print('user created')
        return  render(request,"login.html")
    else:
          print('password is not matching')
    return render(request,"register.html")


def login(request):

     if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenicate(username=username, password=password)


            return render(request,"newpage.html")

     else:
        return render(request,"login.html")

def newpage(request):

    if request.method == 'POST':

        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phonenumber= request.POST['phonenumber']
        mailid = request.POST['mailid']
        address = request.POST['address']
        department = request.POST['slct1']
        course = request.POST['slct2']
        purpose = request.POST["purpose"]
        materials = request.POST['materials']


    return render(request, "newpage.html")


