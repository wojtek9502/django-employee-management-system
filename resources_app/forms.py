from django import forms
from resources_app import models
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from dal import autocomplete

class ResourceCreateForm(forms.ModelForm):
    class Meta:
        model = models.ResourceModel
        fields = ['is_available', 'name', 'production_year', 'resource_state', 'image', 'brand', 'model', 'info']
        widgets = {
            'approver_user': autocomplete.ModelSelect2(
                url='user_admin_autocomplete',
                attrs={
                    'data-minimum-input-length': 3,
                    },
                ),
            
            'production_year': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }


    # def clean(self):
    #     start_date = self.cleaned_data.get("start_date")
    #     end_date = self.cleaned_data.get("end_date")
    #     print(start_date, end_date)
    #     if end_date < start_date:
    #         msg = "Data rozpoczęcia jest póżniejsza niż data zakończenia"
    #         self._errors["end_date"] = self.error_class([msg])
