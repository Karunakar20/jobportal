from rest_framework.views import APIView, Response

from api.controller.users.login import LoginController
from api.controller.users.logout import LogoutController

class ApiLogin(APIView):
     
     def post(self,request):
          pData = request.data

          ret = LoginController(pData).login()
          return Response(ret.toJson())
     
class ApiLogout(APIView):
     
     def post(self,request):
          id = request.query_params.get('id',None)

          ret = LogoutController(id).logout()
          return Response(ret.toJson())
     
          