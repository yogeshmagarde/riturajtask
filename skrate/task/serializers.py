
from.models import Registration,Ticket
from rest_framework import serializers

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ['url','username','role']

class Ticketserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url','title','status','priority','assinedTo','createdAt']

