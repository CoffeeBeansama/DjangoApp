from django.urls import path
from . import views 
from . import settings



urlpatterns = [
    path("",views.home,name="home"),
    path("add/",views.addMember,name="addmember"),
    path("add/addrecord/",views.addRecord,name="addrecord"),
    path("update/<int:id>",views.update,name="update"),
    path("update/updaterecord/<int:id>",views.updateRecord,name="updaterecord"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("delete/deleterecord/<int:id>",views.deleteRecord,name="deleterecord"),
]
