from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Użytkownik', related_name='user_profile')
    pesel = models.CharField(max_length=11, verbose_name='PESEL')
    street = models.CharField(max_length=200, verbose_name='Ulica')
    city = models.CharField(max_length=200, verbose_name='Miasto')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    post_code = models.CharField(max_length=6, verbose_name='Kod pocztowy')


    def __str__(self):
        return self.user.get_full_name() + ',  PESEL: ' + self.pesel