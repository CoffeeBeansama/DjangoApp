from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import models
from . import settings

# Create your views here.

def index(request):
    return HttpResponse(loader.get_template("misc/index.html").render({},request))
    
def home(request):
    members = models.Member.objects.all().values()
    template = loader.get_template("members/home.html")
    context = {
        "members" : members
    }

    return HttpResponse(template.render(context,request))

def addMember(request):
    template = loader.get_template("members/add.html")
    return HttpResponse(template.render({},request))

def addRecord(request):
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]

    member = models.Member(firstName=firstName,lastName=lastName)
    member.save()
    return HttpResponseRedirect(reverse("home"))

def update(request,id):
    member = models.Member.objects.get(id=id)
    template = loader.get_template("members/update.html")
    context = {
        "member" : member
    }
    return HttpResponse(template.render(context,request))

def updateRecord(request,id):
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]

    member = models.Member.objects.get(id=id)
    member.firstName = firstName
    member.lastName = lastName
    member.save()
    return HttpResponseRedirect(reverse("home"))
