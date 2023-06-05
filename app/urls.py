from django.urls import path

from .views import *

urlpatterns = [
    path('',home_page,name="home_page"),
    path('add/question/',add_question,name="add_question"),
    path('result/',result,name="result"),
    path('user/permissions/',user_permissions,name="user_permissions"),
    path('user/approve/<int:id>/',approve_sts,name="approve_sts"),
]