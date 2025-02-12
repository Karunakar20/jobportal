
from django.urls import path

from api.views.users.register import ApiRegister
from api.views.users.login_logout import ApiLogin,ApiLogout
from api.views.jobs.jobs import ApiJob

urlpatterns = [
    path('register/', ApiRegister.as_view()),
    path('login/',ApiLogin.as_view()),
    path('logout/',ApiLogout.as_view()),
    path('publish/',ApiJob.as_view()),
    

]
