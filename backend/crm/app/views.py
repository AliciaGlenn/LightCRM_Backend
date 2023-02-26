from django.shortcuts import render
from django.http import JsonResponse ## For Sending Json Responses
from django.views import View ## Allows our class to act as a view
from .helpers import GetBody

class HomeView(View):
    def main_route (request):
     render(request, "index.html")

class FirstView(View):
    #since the methods name is "get" it will run on "get" requests
    def get(self, request):
        return JsonResponse({"hello":"world", "method": request.method})

    #since the methods name is "post" it will run on "post" requests
    def post(self, request):
        return JsonResponse({"hello":"world", "method": request.method})

    #since the methods name is "put" it will run on "put" requests
    def put(self, request):
        return JsonResponse({"hello":"world", "method": request.method})

    #since the methods name is "delete" it will run on "delete" requests
    def delete(self, request):
        return JsonResponse({"hello":"world", "method": request.method})
    
    
class SecondView(View):
        def get(self, request, param):
            return JsonResponse({"param": param})
        
        
class ThirdView(View):
        def get(self, request):
            return JsonResponse({"third":"three", "method": request.method})
        
# class for "/contact/<id>" routes
class ContactViewID(View):
    ## Function to show 1 contact
    def get (self, request, id):
        ## get the contact
        contact = Contact.objects.get(id=id)
        ## serilize then turn into dictionary
        finalData = json.loads(serialize("json", [contact]))
        ## send json response
        return JsonResponse(finalData, safe=False)

    ## Function for updating contact
    def put (self, request, id):
        ## get the body
        body = GetBody(request)
        ##update contact
        ## ** is like JS spread operator
        Contact.objects.filter(id=id).update(**body)
        ## query for contact
        contact = Contact.objects.get(id=id)
        ## serialize and make dict
        finalData = json.loads(serialize("json", [contact]))
        ## return json data
        return JsonResponse(finalData, safe=False)

    def delete (self, request, id):
        ## query the contact
        contact = Contact.objects.get(id=id)
        ## delete the contact
        contact.delete()
        ## serilize and dict updated contact
        finalData = json.loads(serialize("json", [contact]))
        ##send json response
        return JsonResponse(finalData, safe=False)
    
