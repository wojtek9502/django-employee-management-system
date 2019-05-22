from django.db import models
from accounts.models import MyUser

# Create your models here.

class ProjectModel(models.Model):
    id_employee = models.ManyToManyField(MyUser,  verbose_name='Pracownik', related_name='project_employee_user')
    id_project_pm = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, verbose_name='Manager projektu', related_name='project_pm_user', null=True, blank=True)
    client = models.CharField(max_length=300, verbose_name='Nazwa klienta')
    name = models.CharField(max_length=200, verbose_name='Nazwa')
    number = models.IntegerField(verbose_name='Numer projektu')
    number_2 = models.IntegerField(verbose_name='Numer projektu 2')
    project_type = models.CharField(max_length=50, verbose_name='Typ projektu')
    status = models.CharField(max_length=50, verbose_name='Status')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    end_date = models.DateField(verbose_name='Data zakończenia')
    contact = models.CharField(max_length=500, verbose_name='Kontakt')
    commants = models.CharField(max_length=500, verbose_name='Uwagi', null=True, blank=True)

    def __str__(self):
        return self.name+" number: "+ str(self.number) +" number2: " + str(self.number_2) + " project_pm: " + self.id_project_pm.get_full_name()

class HolidayModel(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='holiday_user')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='holiday_approver_user')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    end_date = models.DateField(verbose_name='Data zakończenia')
    is_used = models.BooleanField(default=False, verbose_name='Czy zakończone')
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')
