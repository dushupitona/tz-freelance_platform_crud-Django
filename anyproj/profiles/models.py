from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ExecutorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone  = PhoneNumberField(region='RU')

    experience = models.PositiveIntegerField()
    exp_description = models.TextField()
    
    def __str__(self):
        return self.user.username
    

class CustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone  = PhoneNumberField(region='RU')

    def __str__(self):
        return self.user.username