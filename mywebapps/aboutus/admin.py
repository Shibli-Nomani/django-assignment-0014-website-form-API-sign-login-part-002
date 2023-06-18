from django.contrib import admin

#registers models in admin directory
from . models import Guides, Destination, Package
# Register your models here.
#one to one relationship
@admin.register(Guides)
class guideAdmin(admin.ModelAdmin):
    list_display = ['guide_name', 'guide_reg', 'user']

#Many to One relationship
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['destination_name', 'destination_code', 'packages', 'user']

#Many to Many relationship
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'package_code', 'guide_package_user']

    