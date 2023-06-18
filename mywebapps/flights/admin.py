from django.contrib import admin

from .models import Flight

#to see the proper table format

class FlightAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'client_id', 'client_name', 'client_email',
                      'batch', 'destination')

# Register your models here.

admin.site.register(Flight, FlightAdmin)

#import class for specific model
from .models import AgentInfo


#to see the proper table format
class AgentInfoAdmin(admin.ModelAdmin):

    list_display = ( 'first_name', 'last_name',  'email', 'acode',  'mobile', 
                    'password', 're_password',  'textarea',  'checkbox', 
                    'registration_fee', 'agree')

# Register your models here.

admin.site.register(AgentInfo, AgentInfoAdmin)