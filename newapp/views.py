from django.shortcuts import render
from django.http import HttpResponse
from . task import test_fun,test_email
# Create your views here.


def test(request):
    test_fun.delay()
    return HttpResponse("done")



def send_mail(request):
    test_email.delay()
    return HttpResponse("email done")