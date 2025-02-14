from rest_framework.views import APIView, Response
from api.controller.jobs.apply_jobs import ApplyJobsController


class ApiApplyJobs(APIView):
     
     def post(self,request):
          
          cmd = request.query_params.get('cmd',None)
          pData = request.data
          data = {
               "cmd":cmd,
               "data":pData,
               
          }
          
          ret = ApplyJobsController(data).manage()
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
          
          ret = ApplyJobsController(data).get()
          return Response(ret.toJson())
          
          
          