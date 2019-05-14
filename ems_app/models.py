from django.db import models
from accounts.models import MyUser

# Create your models here.

class ProjectsModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nazwa')
    number = models.IntegerField(verbose_name='Numer projektu')
    number_2 = models.IntegerField(verbose_name='Numer projektu 2')
    project_type = models.CharField(max_length=50, verbose_name='Typ projektu')
    status = models.CharField(max_length=50, verbose_name='Status')
    start_date = models.DateField()
    end_date = models.DateField()
    client_pm = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='PM Klienta', related_name='client_pm_user')
    project_pm = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='PM Projektu', related_name='project_pm_user')
    contact = models.CharField(max_length=500, verbose_name='Kontakt')
    commants = models.CharField(max_length=500, verbose_name='Uwagi', null=True, blank=True)

    def __str__(self):
        return self.name+" number: "+ self.number +" number2: " + self.number_2 + " project_pm: " + self.project_pm
