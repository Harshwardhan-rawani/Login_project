from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from app.models import data
def loginpage(request):
    return render(request,'loginpage.html')
def create(request):
    return render(request,'create.html')
def submitform(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('tel')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            a=data(Name=name,Phone=phone,Email=email,Password=password,Confirm_Password=password)
            a.save()
            return render(request,'create.html')
        else:
            invalid="Password didn't match"
            return render(request,'create.html',{'error':invalid})
        
def submitloginform(request):
    
    a=data.objects.all()

    if request.method=="POST":
        loginemail=request.POST.get('loginEmail')
        loginpassword=request.POST.get('loginPassword')

        for x in a:
            if x.Email != loginemail and x.Password != loginpassword:
                Both_invalid="Invalid Email and Password"
                return render(request,'loginpage.html',{'error':Both_invalid})
            elif(x.Email != loginemail):
                E_invalid="Invalid Email"
                return render(request,'loginpage.html',{'error':E_invalid})
            elif(x.Password !=loginpassword):
                P_invalid="Invalid Password"
                return render(request,'loginpage.html',{'error':P_invalid})
            else:
                return render(request,'thank.html',{'name':x.Name})


                


        


    