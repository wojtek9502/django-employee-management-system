from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

#create your own user class.
class MyUser(AbstractUser):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('email').blank = False
        self._meta.get_field('email')._unique = True
        super(MyUser, self).__init__(*args, **kwargs)

    class Meta:
       app_label = 'accounts'

    def __str__(self):
        return "ID: " + str(self.id) +  " " + self.get_full_name() 

class UserStateModel(models.Model):
    state_description = models.CharField(max_length=50, verbose_name='Stan użytkownika')

    def __str__(self):
            return self.state_description

class WorkHoursModel(models.Model):
    description = models.CharField(max_length=200, verbose_name='Opis zmiany')
    rate_of_pay = models.DecimalField(verbose_name='Stawka płacy', default=1.00, max_digits=3, decimal_places=2)

    def __str__(self):
            return self.description

class UserProfileInfo(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name='Użytkownik', related_name='user_profile')
    user_manager = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Kierownik', related_name='user_manager')
    user_work_hours = models.ForeignKey(WorkHoursModel, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Godziny pracy', related_name='user_work_hours')
    user_state = models.ForeignKey(UserStateModel, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Stan użytkownika', related_name='user_state')
    pesel = models.CharField(max_length=11, verbose_name='PESEL')
    street = models.CharField(max_length=200, verbose_name='Ulica')
    city = models.CharField(max_length=200, verbose_name='Miasto')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    post_code = models.CharField(max_length=6, verbose_name='Kod pocztowy')
    house_number = models.CharField(max_length=20, verbose_name='Numer domu')
    image = models.ImageField(upload_to='avatars/', default=None, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() + ',  PESEL: ' + self.pesel

class UserAccessModel(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, verbose_name='Użytkownik', related_name='user_access')
    rfid = models.CharField(max_length=200, verbose_name='rfid')
    comments = models.CharField(max_length=500, verbose_name='uwagi', null=True, blank=True)

    def __str__(self):
            return self.user.get_full_name() + ',  PESEL: ' + self.pesel


