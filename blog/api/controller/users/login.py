from api.common.meta import PortalResponse, PortalResponseType
from django.contrib.auth import authenticate

class LoginController:
     
     def __init__(self, pData):
          self.data = pData
     
     def __getData(self):
          self.username = self.data.get('username', None)
          self.password = self.data.get('password', None)

     def login(self):
          self.__getData()
          try:
               user = authenticate(username=self.username, password=self.password)
               if not user:
                    return PortalResponse(False, PortalResponseType.err, "Invalid username or password", None)
               
               return PortalResponse(True, PortalResponseType.success, "Login successful", None)

          except Exception as e:
               return PortalResponse(False, PortalResponseType.err, f"Error: {str(e)}", None)
