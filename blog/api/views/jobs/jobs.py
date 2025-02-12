from rest_framework.views import APIView,Response
from api.controller.jobs.jobs import JobController

class ApiJob(APIView):
     
     def post(self,request):
          data = request.data
          id = request.query_params.get('id',None)
          cmd = request.query_params.get('cmd',None)
          
          pData = {
               "data":data,
               "id":id,
               "cmd":cmd
          }
          res = JobController(pData).manage()
          return Response(res.toJson())
          
     