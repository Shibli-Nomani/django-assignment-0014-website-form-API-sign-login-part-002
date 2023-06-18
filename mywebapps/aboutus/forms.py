from django.contrib.auth.models import User
#for user registration
from django.contrib.auth.forms import UserCreationForm
#for user login
#from django.contrib.auth.forms import AuthenticationForm


#to create modified class of UserCreationForm and use it to views.py
class usercf(UserCreationForm):
    class Meta:
        model = User
        #to call field for user input; field name should be as per UserCreationForm
        fields = ['username', 'email', 'first_name', 'last_name']

