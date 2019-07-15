from django.db import models
from accounts.models import MyUser
from project_app.models import ProjectModel
from resources_app.models import ResourceModel


class EntranceExitReason(models.Model):
    reason_description = models.CharField(max_length=200, verbose_name='opis')

    def __str__(self):
        return self.reason_description

class EntranceExitModel(models.Model):
    resource = models.ManyToManyField(ResourceModel, blank=True, default=None, verbose_name='Zasób', related_name='entrance_exit_resource')
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Pracownik', related_name='entrance_exit_user')
    reason = models.ForeignKey(EntranceExitReason, on_delete=models.DO_NOTHING, verbose_name='Powód', related_name='entrance_exit_reason')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, verbose_name='Osoba zatwierdzająca', related_name='entrance_exit_approver_user')
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, verbose_name='Projekt', related_name='entrance_exit_project')
    start_date = models.DateTimeField(verbose_name='Data rozpoczęcia')
    end_date = models.DateTimeField(verbose_name='Data zakończenia')
    is_approved = models.BooleanField(default=False, verbose_name='Czy zatwierdzone')
    place = models.CharField(max_length=200, verbose_name='Miejsce')
    fromExitToEntranceTimestamp = models.IntegerField(verbose_name='Czas', null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.get_full_name()) + " PESEL " + str(self.user.user_profile.pesel) + " powód: " + str(self.reason)
