from django import forms
from holiday_app import models
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from dal import autocomplete

class HolidayForm(forms.ModelForm):
    class Meta:
        model = models.HolidayModel
        fields = '__all__'
        widgets = {
            'approver_user': autocomplete.ModelSelect2(
                url='user_admin_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),

            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

    def __init__(self, user, *args, **kwargs):
        #jesli user nie jest adminem to moze zaplanowac urlop tylko sobie, i nie ma pol
        #w widoku trzeba przeslonic metode get_form_kwargs() aby dodac usera do formularza
        super(HolidayForm, self).__init__(*args, **kwargs)
        if user.is_superuser == False:
            self.fields['user'].queryset = models.MyUser.objects.filter(id=user.id)
            self.fields.pop('is_used')
            self.fields.pop('is_approved')

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        print(start_date, end_date)
        if end_date < start_date:
            msg = "Data rozpoczęcia jest póżniejsza niż data zakończenia"
            self._errors["end_date"] = self.error_class([msg])
