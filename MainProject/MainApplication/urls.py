from django.urls import path
from . import views 

pageName = "Greet User"


urlpatterns = [
    path('', views.greet,name=pageName),
]
