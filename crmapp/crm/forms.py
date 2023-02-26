from .models import Contact
from django.forms import ModelForm

class ContactForm(ModelForm): 
    class Meta:
     model = Contact
     fields = ["companyName", "person", "personTitle", "emailAddress", "usState"]
    
