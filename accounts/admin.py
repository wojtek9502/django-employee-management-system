from django.contrib import admin
from accounts import models

# Register your models here.

admin.site.register(models.UserProfileInfo)
admin.site.register(models.MyUser)
admin.site.register(models.UserAccess)

