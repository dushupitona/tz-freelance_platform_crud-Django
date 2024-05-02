from django.contrib import admin

from profiles.models import ExecutorModel, CustomerModel

# Register your models here.


admin.site.register(ExecutorModel)
admin.site.register(CustomerModel)
