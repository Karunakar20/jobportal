from api.api_models.jobs import Jobs
from django.db import transaction,DatabaseError
from api.common.meta import PortalResponse,PortalResponseType
from datetime import date
from api.api_models.authenticate import Authentcation

class JobController:
     
     def __init__(self,pData):
          self.data = pData['data']
          self.cmd = pData['cmd']
          self.id = pData['id']
          
     def __getData(self):
          self.title = self.data.get('title',None)
          self.description = self.data.get('description',None)
          self.company_name = self.data.get('company_name',None)
          self.experience = self.data.get('experience',None)
          self.salary_range = self.data.get('salary_range',None)
          self.location = self.data.get('location',None)
          self.notice_period = self.data.get('notice_period',None)
          self.openings = self.data.get('openings',None)
          self.education_quaification = self.data.get('education_quaification',None)
          self.applicants = self.data.get('applicants',None)
          self.skills = self.data.get('skills',None)
          
     def __validation(self):
          
          self.auth = Authentcation.objects.filter().first()
          if not self.auth.users.is_recruiter:
               return PortalResponse(False, PortalResponseType.err,"Only recruiter can publish the jobs",None)
          
          if not self.auth.is_login:
               return PortalResponse(False, PortalResponseType.err,"recruiter is not login",None)
          
          return PortalResponse(True, PortalResponseType.err,"Validation is Sucessfull",None)
               
     def __publishJob(self):
          
          self.__getData()
          val = self.__validation()
          
          if not val.ok:
               return PortalResponse(False, PortalResponseType.err,"Validaion failed",None)
          try:
               
               with transaction.atomic():
                    if self.id:
                         jobs = Jobs.objects.filter(id=self.id).first()
                    else:
                         jobs = Jobs()
                    jobs.users = self.auth  
                    jobs.title = self.title
                    jobs.description = self.description
                    jobs.company_name = self.company_name
                    jobs.experience = self.experience
                    jobs.salary_range = self.salary_range
                    jobs.location = self.location
                    jobs.date_of_posted = date.today()
                    jobs.openings = self.openings
                    jobs.notice_period = self.notice_period
                    jobs.education_quaification = self.education_quaification
                    jobs.skills = self.skills
                    
                    jobs.save()

                    return PortalResponse(True, PortalResponseType.success, None, self.sucess)

          except DatabaseError as err:
               return PortalResponse(False, PortalResponseType.err, f"Database error: {str(err)}", None)
          except Exception as ec:
               return PortalResponse(False, PortalResponseType.err, f"Unexpected error: {str(ec)}", None)
          
     def __delete(self):
          self.__validation()
          try:
               with transaction.atomic():
                    
                    jobs = Jobs.objects.get(id=self.id)
                    jobs.delete()
                    return PortalResponse(True, PortalResponseType.success,None,self.sucess)
                    
          
          except DatabaseError as err:
               return PortalResponse(False, PortalResponseType.err,f"Database error: {str(err)}",None)  
          except Exception as ec:
               return PortalResponse(False, PortalResponseType.err, f"Unexpected error: {str(ec)}",None)
          
     
     def manage(self):
          match self.cmd:
               case 'publish':
                    self.sucess = 'Job Published Sucessfully'
                    return self.__publishJob()
               
               case 'update':
                    self.sucess = 'Job Updated Sucessfully'
                    return self.__publishJob()
               
               case 'delete':
                    self.sucess = 'Job Deleted Sucessfully'
                    return self.__delete()
               
               case _:
                    content = 'cmd paramaeter expected, <url>?cmd=<parameter>. parameters: publish, update or delete'
                    mRet = PortalResponse(False, PortalResponseType.err,None,None,content)
                    return mRet
               
     
          
          

          

