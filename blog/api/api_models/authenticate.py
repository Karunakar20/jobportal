from api.api_models.user import PortalUsers
from django.db import models

class Authentcation(models.Model):
     
     users = models.ForeignKey(PortalUsers, on_delete=models.CASCADE, related_name='auth_fk_users')
     is_login = models.BooleanField(default=True)
     
     class Meta:
          db_table = 'db_auth'
