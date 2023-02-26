from django.shortcuts import render
## For sending JSON Responses
from django.http import JsonResponse
## To serialize objects into json strings
from django.core.serializers import serialize
## To turn json strings into dictionaries
import json
## The contact Model
from .models import Contact
## View class
from django.views import View
## GetBody
from .helpers import GetBody

#def GetBody(request):
    # decode the request body into a unicode string
   # unicode = request.body.decode('utf-8')
    # turn the unicode string into a python dictionary
    #return json.loads(unicode)


# class for "/contacts" routes
class ContactView(View):
    ## Route to get all Turtles
    def get(self, request):
        ## get all the Turtles
        all = Contact.objects.all()
        ## Turn the object into a json string
        serialized = serialize("json", all)
        ## Turn the json string into a dictionary
        finalData = json.loads(serialized)
        ## Send json response, turn safe off to avoid errors
        return JsonResponse(finalData, safe=False)

    ## Route to create a turtle
    def post (self, request):
        ## get data from the body
        body = GetBody(request)
        print(body)
        ## create new turtle
        contact = Contact.objects.create(name=body["name"], age=body["age"])
        ## turn the new turtle into json string then a dictionary
        finalData = json.loads(serialize("json", [contact])) #turtle in array to be serializable
        ## Send json response
        return JsonResponse(finalData, safe=False)