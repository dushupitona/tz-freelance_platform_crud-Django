from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField


class ExecutorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone  = PhoneNumberField(region='RU')

    experience = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    exp_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    @classmethod
    def slug(cls):
        return 'executor'
    

class CustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone  = PhoneNumberField(region='RU')

    def __str__(self):
        return self.user.username
    
    @classmethod
    def slug(cls):
        return 'customer'
    


