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
    commants = models.CharField(max_length=500, verbose_name='Uwagi', null=True, blank=True)

    def __str__(self):
        return self.name+" number: "+ str(self.number) +" number2: " + str(self.number_2) + " project_pm: " + self.id_project_pm.get_full_name()

class HolidayModel(models.Model):
    user = models.OneToOneField(MyUser, null=True, blank=True, default=None, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='holiday_user')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='holiday_approver_user')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    end_date = models.DateField(verbose_name='Data zakończenia')
    is_used = models.BooleanField(default=False, verbose_name='Czy zakończone')
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')

    def __str__(self):
        return "Wolne: " + self.user.get_full_name() + " PESEL: " + self.user.user_profile.pesel + "  od: " + str(self.start_date) + " do: " + str(self.end_date)

class ResourceStateModel(models.Model):
    state_description = models.CharField(max_length=50, verbose_name='Stan zasobu')

    def __str__(self):
        return self.state_description


class ResourceModel(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, verbose_name='Pracownik', related_name='resource_user')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='resource_approver_user')
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')
    is_available = models.BooleanField(default=True, verbose_name='Czy dostępny')
    name = models.CharField(max_length=200, default=None, verbose_name='Nazwa zasobu')
    start_date = models.DateField(default=None, null=True, blank=True, verbose_name='Data przydzielenia')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='Data zakończenia')
    production_year = models.DateField(verbose_name='Data produkcji', default=None, null=True, blank=True)
    resource_state = models.ForeignKey(ResourceStateModel, on_delete=models.DO_NOTHING, verbose_name='Stan zasobu', related_name='resource_state') 
    image = models.ImageField(upload_to='resources/', default=None, null=True, blank=True, verbose_name="Zdjęcie")
    brand = models.CharField(max_length=200, default=None, verbose_name='Marka zasobu')
    model = models.CharField(max_length=200, default=None, verbose_name='Model zasobu')
    info =  models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name='Dodatkowe informacje')

    def __str__(self):
        return self.name + " stan: " + str(self.resource_state) + " czy_dostepny: "  + str(self.is_available)

class ResourceHistoryModel(models.Model):
    resource = models.ForeignKey(ResourceModel, on_delete=models.DO_NOTHING, verbose_name='Zasób')
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='resource_history_user')
    start_date = models.DateField(default=None, null=True, blank=True, verbose_name='Data przydzielenia')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='Data zakończenia')
    approver_user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Osoba zatwierdzająca', related_name='resource_history_approver_user')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    end_date = models.DateField(verbose_name='Data zakończenia')
    
    def __str__(self):
        return str(self.resource)


class FuelType(models.Model):
    fuel_type_description = models.CharField(max_length=100, verbose_name='Typ paliwa')
    
    def __str__(self):
        return self.fuel_type_description

class AutoModel(models.Model):
    resource = models.OneToOneField(ResourceModel, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='resource_auto')
    fuel_type = models.ForeignKey(FuelType, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Rodzaj paliwa', related_name='auto_fuel_type') 
    fuel_card_number = models.IntegerField(verbose_name='Numer karty paliwa')
    registration_number = models.CharField(max_length=30, verbose_name='Numer rejestracyjny')
    car_meter_status = models.DecimalField(verbose_name='Stan licznika', max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.resource)


class EntranceExitReason(models.Model):
    reason_description = models.CharField(max_length=200, verbose_name='Miejsce')

    def __str__(self):
        return self.reason_description

class EntranceExitModel(models.Model):
    resource = models.ManyToManyField(ResourceModel, blank=True, default=None, verbose_name='Zasób', related_name='entrance_exit_resource')
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='entrance_exit_user')
    reason = models.ForeignKey(EntranceExitReason, on_delete=models.DO_NOTHING, verbose_name='Powód', related_name='entrance_exit_reason')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='entrance_exit_approver_user')
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, verbose_name='Projekt', related_name='entrance_exit_project')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')
    place = models.CharField(max_length=200, verbose_name='Miejsce')
    fromExitToEntranceTimestamp = models.IntegerField(verbose_name='Czas', null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.get_full_name()) + " PESEL " + str(self.user.user_profile.pesel) + " powód: " + str(self.reason)