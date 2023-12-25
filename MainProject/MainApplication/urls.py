from django.urls import path
from . import views 
from . import settings



urlpatterns = [
    path("",views.home,name="home"),
    path("add/",views.addOrder,name="addorder"),
    path("add/addrecord/",views.addOrder,name="addrecord"),
    path("update/<int:id>",views.update,name="update"),
    path("update/updaterecord/<int:id>",views.updateOrder,name="updaterecord"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("delete/deleterecord/<int:id>",views.deleteOrder,name="deleterecord"),
]
