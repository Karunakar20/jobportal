from django.contrib import admin
from api.api_models.user import PortalUsers
from api.api_models.authenticate import Authentcation
from api.api_models.jobs import Jobs
from api.api_models.apply_jobs import JobsApply
# Register your models here.

admin.site.register(PortalUsers)
admin.site.register(Authentcation)
admin.site.register(Jobs)
admin.site.register(JobsApply)

