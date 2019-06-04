from django.db import models
from accounts.models import MyUser

# Create your models here.
class HolidayModel(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='holiday_user')
    approver_user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='holiday_approver_user')
    start_date = models.DateField(verbose_name='Data rozpoczęcia')
    end_date = models.DateField(verbose_name='Data zakończenia')
    is_used = models.BooleanField(default=False, verbose_name='Czy zakończone')
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')

    def __str__(self):
        return "Wolne: " + self.user.get_full_name() + " PESEL: " + self.user.user_profile.pesel + "  od: " + str(self.start_date) + " do: " + str(self.end_date)
