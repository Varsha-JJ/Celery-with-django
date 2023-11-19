from django.urls import path 
from .views import test ,send_mail


urlpatterns = [
    path('',test,name="test"),
    path('send/',send_mail,name="send_mail")
]