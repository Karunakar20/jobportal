from api.api_models.jobs import Jobs
from django.db import models

class StatusIntegerChoice(models.IntegerChoices):
    VIEW = 1
    APPLIED = 2

class JobsApply(models.Model):
    job_list = models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name='jobs_apply_fk_jobs')
    status = models.IntegerField(choices=StatusIntegerChoice.choices)
    is_applied = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'db_jobs_apply'