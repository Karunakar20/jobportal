from api.common.meta import PortalResponse, PortalResponseType
from api.api_models.user import PortalUsers
from api.api_models.authenticate import Authentcation
from django.db import DatabaseError, transaction
class LoginController:
     
     def __init__(self, pData):
          self.data = pData
     
     def __getData(self):
          self.username = self.data.get('username', None)
          self.password = self.data.get('password', None)

     def login(self):
          self.__getData()
          try:
               with transaction.atomic():
                    user = PortalUsers.objects.filter(username=self.username).first()
                    if not user:
                         return PortalResponse(False, PortalResponseType.err, "Username is notmachng", None)
                    elif not user.password == self.password:
                         return PortalResponse(False, PortalResponseType.err, "Password is not not matching", None)
                    
                    auth = Authentcation.objects.filter(users=user).first()
                    if auth:
                         auth.is_login = True
                    else:
                         auth = Authentcation(users=user, is_login=True)
                    
                    auth.save()
                    
                    return PortalResponse(True, PortalResponseType.success, "Login successful", None)
               
          except DatabaseError as err:
               return PortalResponse(False, PortalResponseType.err,f"Database error: {str(err)}",None)  

          except Exception as e:
               return PortalResponse(False, PortalResponseType.err, f"Error: {str(e)}", None)
