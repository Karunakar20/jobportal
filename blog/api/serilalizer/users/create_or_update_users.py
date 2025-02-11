from rest_framework import serializers
from api.api_models.user import PortalUsers

class SrUsers(serializers.ModelSerializer):
     class Meta:
          model = PortalUsers
          fields = ['id']
     def to_representation(self, instance:PortalUsers):
          ret = super().to_representation(instance)
          
          ret['username'] = instance.username if instance.username else None
          ret['password'] = instance.password if instance.password else None
          ret['display_name'] = instance.display_name if instance.display_name else None
          
          return ret