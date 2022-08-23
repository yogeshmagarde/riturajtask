from random import choices
from secrets import choice
from django.db import models

ROLE_CHOICE = (
    ('admin','admin'),
    ('employee','employee'),
)

STATUS_CHOICE = (('open','open'),
('close','close'),
)

PRIORITY_CHOICE = (('low','low'),('medium','medium'),
('high','high'),
)

class Registration(models.Model):
    username = models.CharField(max_length=50)
    role = models.CharField(choices=ROLE_CHOICE,max_length=50)
    
class Ticket(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICE,max_length=50)
    priority = models.CharField(choices=PRIORITY_CHOICE,max_length=50)
    assinedTo = models.ForeignKey(Registration,on_delete=models.CASCADE)
    createdAt = models.TimeField()

