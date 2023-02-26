from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if (request.method == "POST"):
        Contact.objects.create(
            companyName=request.POST.get("companyName"),
            person=request.POST.get("person"),
            personTitle=request.POST.get("personTitle"),
            emailAddress=request.POST.get("emailAddress"),
            usState=request.POST.get("usState")
        )
        return HttpResponseRedirect("/contacts/")
    if (request.method == "GET"):
        contacts = Contact.objects.all()
        form = ContactForm()
        return render(request, "index.html", {"contacts": contacts, "form": form })

def destroy(request, id):
    Contact.objects.destroy(id)
    return HttpResponseRedirect("/contacts/")