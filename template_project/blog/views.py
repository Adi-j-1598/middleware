from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
def home(request):
    print('I am view')
    return HttpResponse('Hello World')


def excp(request):
    print('I am Exception view')
    a=20/0
    return HttpResponse('This is Exception Page')



def user_info(request):
    print('I am user info view')
    context={'name':'Aditya'}
    return TemplateResponse(request,'user.html',context)