from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("Francis Aigo R. Miradora")
    



