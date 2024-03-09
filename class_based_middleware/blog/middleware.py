# Function based my_middleware


# def my_middleware(get_response):
#     print('One time initialization')
#     def my_function(request):
#         print('This is before view')
#         response=get_response(request)
#         print('This is after view')
#         return response
#     return my_function
from django.shortcuts import HttpResponse

class MyxMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time x initialization')
    def __call__(self, request):
        print('this is before x view')
        response=self.get_response(request)
        print('This is after x view')
        return response
    

class MyyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time y initialization')
    def __call__(self, request):
        print('this is before y view')
        response=HttpResponse('Nikal lo')
        print('This is after y view')
        return response


class MyzMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time  z initialization')
    def __call__(self, request):
        print('this is before z view')
        response=self.get_response(request)
        print('This is after z view')
        return response