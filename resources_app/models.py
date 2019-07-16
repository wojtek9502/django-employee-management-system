from django.db import models
from accounts.models import MyUser

# Create your models here.
class ResourceStateModel(models.Model):
    state_description = models.CharField(max_length=50, verbose_name='Stan zasobu')

    def __str__(self):
        return self.state_description

class ResourceModel(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, verbose_name='Pracownik', related_name='resource_user')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='resource_approver_user')
    resource_state = models.ForeignKey(ResourceStateModel, on_delete=models.DO_NOTHING, verbose_name='Stan zasobu', related_name='resource_state') 
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')
    is_available = models.BooleanField(default=True, verbose_name='Czy dostępny')
    name = models.CharField(max_length=200, default=None, verbose_name='Nazwa zasobu')
    start_date = models.DateField(default=None, null=True, blank=True, verbose_name='Data przydzielenia')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='Data zakończenia')
    production_year = models.DateField(verbose_name='Data produkcji')
    image = models.ImageField(upload_to='resources/', default=None, null=True, blank=True, verbose_name="Zdjęcie")
    brand = models.CharField(max_length=200, default=None, verbose_name='Marka zasobu')
    model = models.CharField(max_length=200, default=None, verbose_name='Model zasobu')
    info =  models.TextField(max_length=500, verbose_name='Uwagi', null=True, blank=True)

    def __str__(self):
        is_available_desc = ""
        if(self.is_available):
            is_available_desc = "TAK"
        else:
            is_available_desc = "NIE"
        return self.name + " stan: " + str(self.resource_state) + " czy dostepny: "  + is_available_desc

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