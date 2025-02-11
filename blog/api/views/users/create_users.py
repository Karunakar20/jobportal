from rest_framework.views import APIView, Response
from api.controller.users.create_or_update_users import CreateUsersController


class ApiCreateUsers(APIView):
     
     def post(self,request):
          
          cmd = request.query_params.get('cmd',None)
          pData = request.data
          data = {
               "cmd":cmd,
               "data":pData,
               "id":None
          }
          
          ret = CreateUsersController(data).manage()
          return Response(ret.toJson())
     
     def get(self,request):
          
          cmd = request.query_params.get('cmd',None)
          pData = request.data
          id = request.query_params.get('id',None)
          data = {
               "cmd":cmd,
               "data":pData,
               "id":id
          }
          
          ret = CreateUsersController(data).get()
          return Response(ret.toJson())
          
          
          