from django.shortcuts import render,HttpResponse

def home(request):
    print("I am view")
    return HttpResponse('xyz')