from django.contrib import admin
from . import models

modelList = [models.Category,
            models.User,
            models.UserProfile,
            models.Product,
            models.Order,
            models.Customer,
            models.Member
            ]

# Register your models here.

for model in modelList:
    admin.site.register(model)

