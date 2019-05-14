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

#Changed the defaults above.
#Give any additional field you want to associate your user with

class UserProfileInfo(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name='Użytkownik', related_name='user_profile')
    pesel = models.CharField(max_length=11, verbose_name='PESEL')
    street = models.CharField(max_length=200, verbose_name='Ulica')
    city = models.CharField(max_length=200, verbose_name='Miasto')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    post_code = models.CharField(max_length=6, verbose_name='Kod pocztowy')
    house_number = models.CharField(max_length=20, verbose_name='Numer domu')
    image = models.ImageField(upload_to='avatars/', default=None, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() + ',  PESEL: ' + self.pesel

class UserAccess(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name='Użytkownik', related_name='user_access')
    rfid = models.CharField(max_length=200, verbose_name='rfid')
    comments = models.CharField(max_length=500, verbose_name='uwagi', null=True, blank=True)

    def __str__(self):
            return self.user.get_full_name() + ',  PESEL: ' + self.pesel
