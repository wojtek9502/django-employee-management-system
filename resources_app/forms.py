from django import forms
from resources_app import models
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from dal import autocomplete

class ResourceCreateForm(forms.ModelForm):
    class Meta:
        model = models.ResourceModel
        fields = ['name', 'production_year', 'image', 'brand', 'model', 'info', 'is_available']
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
