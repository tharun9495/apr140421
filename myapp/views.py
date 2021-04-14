from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def if_demo(request):
    LOGIN= True
    return render(request,"if_demo.html",context={"LOGIN":LOGIN})

def ifelse_demo(request):
    LOGIN = True
    return render(request,"ifelse_demo.html",context={"LOGIN":LOGIN,'a':10,'b':20,'name':"Reddy"})
def for_demo(request):
    return render(request,"for_demo.html",context={'items':['apple','bat','cat','dog'],'profile':{'name':'reddy','age':23}})