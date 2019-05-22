from django.contrib import admin
from ems_app import models

# Register your models here.
admin.site.register(models.ProjectModel)
admin.site.register(models.HolidayModel)