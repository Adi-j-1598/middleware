from django.shortcuts import HttpResponse
class MyprocessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_view(request,*args,**kwargs):
        print('I am process')
        # return HttpResponse('This is before view')
        return None
    


    
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        msg=exception
        class_name=exception.__class__.__name__
        print(class_name)
        return HttpResponse(msg)
    
    


class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_template_response(self,request,response):
        response.context_data['name']="AADI"
        return response