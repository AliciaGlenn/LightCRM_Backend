#The Model class we will inherit from
from django.db import models
from django import forms

#new model class
class Contact(models.Model):
    # define a string field of max 100 characters
    name = models.CharField(max_length=100)
    # define a age that is an integer
    age = models.IntegerField()
    company_name = models.CharField(max_length=100)
    last_contacted = models.DateField()
    point_of_contact = models.CharField(max_length=100)
    status = models.CharField(choices=crmChoices, max_length=1)
    title_= models.CharField(max_length=100)
    priority = models.CharField(choices=priority, max_length=1)
    email_address = models.EmailField()
    us_state = models.CharField(max_length=100)
    notes = forms.CharField(widget=forms.Textarea)
    

class dealModel(models.Model):
    crmChoices = [
        ('A', 'Still Working'),
        ('B', 'Won'),
        ('C', 'Loss'),
    ]
    
class priorityModel(models.Model):
    priority = [
        ('A', 'High Priority'),
        ('B', 'Low Priority'),
    ]