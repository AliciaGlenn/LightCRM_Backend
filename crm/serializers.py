from .models import Contact
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our ContactSerializer
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Contact
        # the fields that should be included in the serialized output
        fields = ['id', 'companyName', 'person', 'personTitle', 'emailAddress', 'usState']
        
        