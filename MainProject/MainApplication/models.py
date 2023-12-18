from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.userName

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.userName

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    referenceNumber = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.referenceNumber

class Customer(models.Model):
    name = models.CharField(max_length=100)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.name

class Member(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

