from django.db import models
from accounts.models import MyUser

# Create your models here.

class ProjectModel(models.Model):
    id_employee = models.ManyToManyField(MyUser,  verbose_name='Pracownik', related_name='project_employee_user')
    id_project_pm = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Manager projektu', related_name='project_pm_user', null=True, blank=True)
    client = models.CharField(max_length=300, verbose_name='Nazwa klienta')
    name = models.CharField(max_length=200, verbose_name='Nazwa')
    number = models.IntegerField(verbose_name='Numer projektu')
    number_2 = models.IntegerField(verbose_name='Numer projektu 2')
    project_type = models.CharField(max_length=50, verbose_name='Typ projektu')
    status = models.CharField(max_length=50, verbose_name='Status')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    end_date = models.DateField(verbose_name='Data zakończenia')
    contact = models.CharField(max_length=500, verbose_name='Kontakt')
    commants = models.TextField(max_length=500, verbose_name='Uwagi', null=True, blank=True)

    def __str__(self):
        return self.name+" number: "+ str(self.number) +" number2: " + str(self.number_2) + " project_pm: " + self.id_project_pm.get_full_name()

