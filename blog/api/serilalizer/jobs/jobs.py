from rest_framework import serializers
from api.api_models.jobs import Jobs
from api.api_models.apply_jobs import JobsApply

class JobsSr(serializers.ModelSerializer):
     
     class Meta:
          model = Jobs
          fields = ['id']
          
     def to_representation(self, instance:Jobs):
          ret = super().to_representation(instance)
          
          ret['title'] = instance.title if instance.title else None
          ret['company_name'] = instance.company_name if instance.company_name else None
          ret['experience'] = instance.experience if instance.experience else None
          ret['salary_range'] = instance.salary_range if instance.salary_range else None
          ret['location'] = instance.location if instance.location else None
          ret['applicants'] = instance.applicants if instance.applicants else 0

          
          return ret

class JobsExtendedSr(serializers.ModelSerializer):
     
     class Meta:
          model = Jobs
          fields = ['id']
          
     def to_representation(self, instance:Jobs):
          ret = super().to_representation(instance)
          
          ret['title'] = instance.title if instance.title else None
          ret['description'] = instance.description if instance.description else None
          ret['company_name'] = instance.company_name if instance.company_name else None
          ret['experience'] = instance.experience if instance.experience else None
          ret['salary_range'] = instance.salary_range if instance.salary_range else None
          ret['location'] = instance.location if instance.location else None
          ret['date_of_posted'] = instance.date_of_posted if instance.date_of_posted else None
          ret['notice_period'] = instance.notice_period if instance.notice_period else None
          ret['openings'] = instance.openings if instance.openings else None
          ret['applicants'] = instance.applicants if instance.applicants else 0
          ret['education_quaification'] = instance.education_quaification if instance.education_quaification else None
          ret['skills'] = instance.skills if instance.skills else None
          
          return ret

