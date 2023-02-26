#The Model class we will inherit from
from django.db import models
from django import forms


#new model class
class Contact(models.Model):
    companyName = models.CharField(max_length=100)
    #lastContacted = models.DateField()
    person = models.CharField(max_length=100)
   # status = models.CharField(max_length=100)
    personTitle = models.CharField(max_length=100)
   # priority = models.CharField(max_length=100)
    emailAddress = models.EmailField()
    usState = models.CharField(max_length=100)
   # notes = forms.CharField(widget=forms.Textarea)
    
   # class dealStatus(models.Model):
    # crmChoices = [
      #  ('A', 'Still Working'),
      #  ('B', 'Won'),
     #   ('C', 'Loss'),
  #  ]
    
#class priorityStatus(models.Model):
   # priority = [
   #     ('A', 'High Priority'),
   #     ('B', 'Low Priority'),
  #  ]