
from django.urls import path

from api.views.users.create_users import ApiCreateUsers
from api.views.users.login import ApiLogin

urlpatterns = [
    path('users/', ApiCreateUsers.as_view()),
    path('login/',ApiLogin.as_view()),

]
