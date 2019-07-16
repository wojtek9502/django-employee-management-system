from django import forms
from entrance_exit_app import models
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from dal import autocomplete

class EntranceExitForm(forms.ModelForm):
    class Meta:
        model = models.EntranceExitModel
        fields = ('user', 'reason', 'approver_user',
                  'project', 'resource', 'place',
                  'start_date', 'end_date', 'is_approved')
        widgets = {
            'approver_user': autocomplete.ModelSelect2(
                url='user_admin_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),
            
            'user': autocomplete.ModelSelect2(
                url='user_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),

            'project': autocomplete.ModelSelect2(
                url='project_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                }
            ),

            'resource': autocomplete.ModelSelect2Multiple(
                url='resource_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                }
            ),

            'start_date': DateTimePickerInput(options = { "dateFormat": "d.m.y H:i",}),
            'end_date': DateTimePickerInput(options = { "dateFormat": "d.m.y H:i",}),
        }

    def __init__(self, user, *args, **kwargs):
        super(EntranceExitForm, self).__init__(*args, **kwargs)
        if user.is_superuser == False:
            self.fields['user'].queryset = models.MyUser.objects.filter(id=user.id)
            self.fields.pop('is_approved')


    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date < start_date:
            msg = "Data rozpoczęcia jest póżniejsza niż data zakończenia"
            self._errors["end_date"] = self.error_class([msg])



class EntranceExitUpdateForm(forms.ModelForm):
    class Meta:
        model = models.EntranceExitModel
        fields = ('user', 'reason', 'approver_user',
                  'project', 'resource', 'place',
                  'start_date', 'end_date', 'is_approved')
        widgets = {
            'approver_user': autocomplete.ModelSelect2(
                url='user_admin_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),

            'user': autocomplete.ModelSelect2(
                url='user_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),
            
            'project': autocomplete.ModelSelect2(
                url='project_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                }
            ),

            'resource': autocomplete.ModelSelect2Multiple(
                url='resource_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                }
            ),

            
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date < start_date:
            msg = "Data rozpoczęcia jest póżniejsza niż data zakończenia"
            self._errors["end_date"] = self.error_class([msg])