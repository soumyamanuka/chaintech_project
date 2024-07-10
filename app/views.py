from django.shortcuts import render,redirect
from .models import *

# Create your views here.
#def IndexView(request):
   # return render(request,"app/index.html")

#def htmlform(request):
 #   return render(request,"app/Forms.html")

def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']

    newuser = Data.objects.create(Name=name,Email=email,Contact=contact)
    return render(request,"app/show.html")

def ShowPage(request):
    all_data=Data.objects.all()
    return render(request,"app/show.html",{'key1':all_data})
