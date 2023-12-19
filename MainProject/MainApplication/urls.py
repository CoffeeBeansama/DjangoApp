from django.urls import path
from . import views 
from . import settings



urlpatterns = [
    path("", views.index,name="main"),
    path("home/",views.home,name="home"),
    path("home/add/",views.addMember,name="addmember"),
    path("home/add/addrecord/",views.addRecord,name="addrecord"),
    path("home/update/<int:id>",views.update,name="update"),
    path("home/update/updaterecord/<int:id>",views.updateRecord,name="updaterecord"),
]
