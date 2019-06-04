from django import forms
from project_app import models
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from dal import autocomplete

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = '__all__'
        widgets = {
            'id_employee': autocomplete.ModelSelect2Multiple(
                url='user_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),

            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        print(start_date, end_date)
        if end_date < start_date:
            msg = "Data rozpoczęcia jest póżniejsza niż data zakończenia"
            self._errors["end_date"] = self.error_class([msg])