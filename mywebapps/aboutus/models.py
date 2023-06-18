from django.db import models

#import user table
from django.contrib.auth.models import User

# Create your models here.

#one to one relationship
class Guides(models.Model):

    #relationship of User(user_auth) table with Guides. 
    # on_delete = mdoels.CASCADE. as we create relationship between User and Guides table, once we delete any row in Guides table, it will break the relationship corresponding row of User table
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    guide_name = models.CharField(max_length=30)
    guide_reg = models.IntegerField()

#many to one relationship
class Destination(models.Model):

    #make relationship between User and Destination Table
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    destination_name = models.CharField(max_length = 60)
    destination_code = models.IntegerField()
    packages = models.CharField(max_length=60)

#many to many relationship

class Package(models.Model):
    #make relationship between Package and User table. No CASCADE requires.
    user = models.ManyToManyField(User)
    package_name = models.CharField(max_length= 30)
    package_code = models.IntegerField()

    #call method under Destination class to see the relation as third table
    def guide_package_user(self):

        #call each user from user list and joining by comma after each user
        return ",".join([str(p) for p in self.user.all()])