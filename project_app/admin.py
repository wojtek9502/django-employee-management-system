from django.contrib import admin
from ems_app import models as core_models
from project_app import models as project_models


# Register your models here.
admin.site.register(project_models.ProjectModel)