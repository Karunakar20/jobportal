from django.db import DatabaseError, transaction
from api.api_models.user import PortalUsers
from api.common.meta import PortalResponse,PortalResponseType
from api.serilalizer.users.create_or_update_users import SrUsers

class CreateUsersController:
     
     def __init__(self,pData):
          self.data = pData['data']
          self.cmd = pData['cmd']
          self.id = pData['id']
          
     def __getData(self):
          self.id = self.data.get('id',None)
          self.username = self.data.get('username',None)
          self.password = self.data.get('password',None)
          self.display_name = self.data.get('display_name',None)
          self.is_recruiter = bool(self.data.get('is_recruiter',False))
     
     def __getAll(self):
          if self.id:
               users = PortalUsers.objects.filter(id=self.id)
          else:
               users = PortalUsers.objects.filter()
          users_data = SrUsers(users,many=True).data
          return PortalResponse(True, PortalResponseType.success,None,{"users":users_data})
          
     def __createorUpdate(self):
          self.__getData()
          
          try:
               with transaction.atomic():
          
                    if self.id:
                         users = PortalUsers.objects.get(id=self.id)
                    else:
                         users = PortalUsers()
                         
                    users.username = self.username
                    users.password = self.password
                    users.display_name = self.display_name
                    users.is_recruiter = self.is_recruiter
                    users.save()
                    
                    return PortalResponse(True, PortalResponseType.success,None,self.sucess)
                    
          except DatabaseError as err:
               if "UNIQUE constraint failed" in str(err):
                    return PortalResponse(False, PortalResponseType.err,"User alredy exist with same password.", None)
               return PortalResponse(False, PortalResponseType.err,f"Database error: {str(err)}",None)  
          except Exception as ec:
               return PortalResponse(False, PortalResponseType.err, f"Unexpected error: {str(ec)}",None)  
                    
     def manage(self):
          
          match self.cmd:
               case 'createOrupdate':
                    self.sucess = "User crate or updated scessfully"
                    return self.__createorUpdate()
               
               case _:
                    content = {'cmd paramaeter expected, <url>?cmd=<parameter>. parameters: createOrupdate'}
                    mRet = PortalResponse(False, PortalResponseType.err,None,content)
                    return mRet
               
     def get(self):
          match self.cmd:
               case 'get':
                    if self.id:
                         return self.__getAll()
                    else:
                         return self.__getAll()
               case _:
                    content = {'cmd paramaeter expected, <url>?cmd=<parameter>. parameters: get'}
                    mRet = PortalResponse(False, PortalResponseType.err,None,content)
                    return mRet
                    
                    