from api.common.meta import PortalResponse, PortalResponseType
from api.api_models.user import PortalUsers
from api.api_models.authenticate import Authentcation
from django.db import DatabaseError, transaction

class LogoutController:
     
     def __init__(self,pId):
          self.id = pId
     
     def logout(self):
          try:
               with transaction.atomic():
                    user = PortalUsers.objects.get(id=self.id)
                    auth = Authentcation.objects.get(users=user)
                    auth.is_login = False
                    
                    auth.save()
                    
                    return PortalResponse(True, PortalResponseType.success, "Logout successful", None)
               
          except DatabaseError as err:
               return PortalResponse(False, PortalResponseType.err,f"Database error: {str(err)}",None)  

          except Exception as e:
               return PortalResponse(False, PortalResponseType.err, f"Error: {str(e)}", None)
