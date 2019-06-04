from django.contrib import admin
from ems_app import models


# Register your models here.
admin.site.register(models.HolidayModel)
admin.site.register(models.ResourceStateModel)
admin.site.register(models.ResourceModel)
admin.site.register(models.FuelType)
admin.site.register(models.AutoModel)
admin.site.register(models.ResourceHistoryModel)
admin.site.register(models.EntranceExitReason)
admin.site.register(models.EntranceExitModel)