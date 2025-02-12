from django.db import models
from api.api_models.authenticate import Authentcation

class Jobs(models.Model):
    
    users = models.ForeignKey(Authentcation, on_delete=models.CASCADE, related_name='jobs_fk_authentcation',null=True,blank=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    company_name = models.CharField(max_length=20)
    experience = models.CharField(max_length=10)
    salary_range = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    date_of_posted = models.DateField()
    notice_period = models.CharField(max_length=50)
    openings = models.CharField(max_length=5)
    applicants = models.IntegerField(null=True,blank=True)
    education_quaification = models.CharField(max_length=10)
    skills = models.CharField(max_length=300)

    class Meta:
        db_table = 'db_jobs'
