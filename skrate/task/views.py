from django.shortcuts import render
# Create your views here.
from.models import Registration,Ticket
from rest_framework import viewsets
from rest_framework import permissions
from task.serializers import Ticketserializer,RegistrationSerializer
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = Ticketserializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
