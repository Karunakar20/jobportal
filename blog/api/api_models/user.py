from django.db import models

class PortalUsers(models.Model):
     username = models.CharField(max_length=30)
     password = models.CharField(max_length=30,unique=True)
     display_name = models.CharField(max_length=30)
     
     class Meta:
          db_table = 'db_portal_users' 