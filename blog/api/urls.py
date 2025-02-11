
from django.urls import path

from api.views.users.create_users import ApiCreateUsers

urlpatterns = [
    path('users/', ApiCreateUsers.as_view()),

]
