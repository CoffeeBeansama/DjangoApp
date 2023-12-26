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
    orders = models.Order.objects.all().values()
    template = loader.get_template("members/home.html")
    context = {
        "orders" : orders
    }

    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template("members/add.html")
    return HttpResponse(template.render({},request))

def addOrder(request):
    product = request.POST["product"]

    newOrder = models.Order(product=product)
    newOrder.save()
    return HttpResponseRedirect(reverse("home"))

def update(request,id):
    order = models.Order.objects.get(id=id)
    template = loader.get_template("members/update.html")
    context = {
        "order" : order
    }
    return HttpResponse(template.render(context,request))

def updateOrder(request,id):
    newProductName = request.POST["order"]

    renewedOrder = models.Order.objects.get(id=id)
    renewedOrder.product = newProductName
    renewedOrder.save()
    return HttpResponseRedirect(reverse("home"))

def delete(request,id):
    order = models.Order.objects.get(id=id)
    template = loader.get_template("members/delete.html")
    context = {
        "order" : order
    }
    return HttpResponse(template.render(context,request))

def deleteOrder(request,id):
    order = models.Order.objects.get(id=id)
    order.delete()
    return HttpResponseRedirect(reverse("home"))

