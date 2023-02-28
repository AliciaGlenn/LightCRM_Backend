from .models import Contact
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactSerializer
#from .forms import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Contact.objects.all()
    # The serializer class for serializing output
    serializer_class = ContactSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]







# Create your views here.
#def index(request):
   # if (request.method == "POST"):
     #   Contact.objects.create(
      #      companyName=request.POST.get("companyName"),
      #      person=request.POST.get("person"),
      #      personTitle=request.POST.get("personTitle"),
      #      emailAddress=request.POST.get("emailAddress"),
      #      usState=request.POST.get("usState")
    #    )
     #   return HttpResponseRedirect("/contacts/")
 #   if (request.method == "GET"):
 #       contacts = Contact.objects.all()
   #     form = ContactForm()
   #     return render(request, "index.html", {"contacts": contacts, "form": form })

#def destroy(request, id):
  #  Contact.objects.get(pk=id).delete()
  #  return HttpResponseRedirect("/contacts/")