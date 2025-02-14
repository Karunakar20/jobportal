from django.db import transaction,DatabaseError

from api.common.meta import PortalResponse,PortalResponseType
from api.api_models.apply_jobs import JobsApply,StatusIntegerChoice
from api.api_models.jobs import Jobs
from api.serilalizer.jobs.jobs import JobsExtendedSr,JobsSr

class ApplyJobsController:
     
     def __init__(self,pData):
          self.data = pData['data']
          self.cmd = pData['cmd']
          self.id = pData['id']
          
     def __getData(self):
          self.id = self.data.get('id',None)
          self.job_list = self.data.get('job_list',None)
          
     def __copy2Jobs(self,obj:JobsApply):
          obj.status = self.status
          obj.job_list = JobsApply.objects.get(id=self.job_list)
          
          if self.status == StatusIntegerChoice.APPLIED.value:
               obj.job_list = True
               
     def __getJob(self):
          if self.id:
               jobs = Jobs.objects.get(id = self.id)
               jobs =JobsExtendedSr(jobs).data
               
          else:
               jobs = Jobs.objects.all()
               jobs =JobsSr(jobs,many=True).data
               
          return PortalResponse(True, PortalResponseType.success,None,None,{"jobs":jobs})
               
     def __viewOrapply(self):
          count = 0
          
          self.__getData()
          try:
               with transaction.atomic():
                    if self.id:
                         self.jApply = JobsApply.objects.get(id=self.id)
                         
                         if self.status in StatusIntegerChoice.APPLIED.value:
                              self.jApply.job_list.applicants += count
                              
                         self.__copy2Jobs(self.jApply)
                         self.jApply.save()
   
                    return PortalResponse(True, PortalResponseType.success, None, self.sucess)

          except DatabaseError as err:
               return PortalResponse(False, PortalResponseType.err, f"Database error: {str(err)}", None)
          except Exception as ec:
               return PortalResponse(False, PortalResponseType.err, f"Unexpected error: {str(ec)}", None)
          
     def manage(self):
          
          match self.cmd:
               
               case 'applied':
                    self.sucess = 'Application Sent sucessfully'
                    self.status = StatusIntegerChoice.APPLIED.value
                    return self.__viewOrapply()
               
               case _:
                    content = 'cmd paramaeter expected, <url>?cmd=<parameter>. parameters: view or applied'
                    mRet = PortalResponse(False, PortalResponseType.err,None,None,content)
                    return mRet
               
     def get(self):
          match self.cmd:
               case 'get_jobs':
                    if self.id:
                         return self.__getJob()
                    else:
                         return self.__getJob()
                    
               case _:
                    content = 'cmd paramaeter expected, <url>?cmd=<parameter>. parameters: get_jobs'
                    mRet = PortalResponse(False, PortalResponseType.err,None,None,content)
                    return mRet
          
     
                    
          
               
          
          
          