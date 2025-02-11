from api.controller.users.login import LoginController
from rest_framework.views import APIView, Response

class ApiLogin(APIView):
     
     def post(self,request):
          pData = request.data

          ret = LoginController(pData).login()
          return Response(ret.toJson())
          