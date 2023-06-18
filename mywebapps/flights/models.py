from django.db import models

# Create your models here.
#table name
#inherit the models into Model
class Flight(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length = 50)
    client_email = models.EmailField(max_length = 35)
    batch = models.IntegerField()
    destination = models.CharField(max_length = 25)

class AgentInfo(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    acode = models.IntegerField()
    mobile = models.IntegerField()  
    password = models.CharField(max_length=15)
    re_password = models.CharField(max_length=15)
    textarea = models.CharField(max_length=100)
    checkbox = models.CharField(max_length=50)
    registration_fee = models.DecimalField(max_digits= 6, decimal_places= 2)
    agree = models.BooleanField()

    
    

