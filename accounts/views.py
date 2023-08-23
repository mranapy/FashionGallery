from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def userhome(request):
    return HttpResponse('OK')