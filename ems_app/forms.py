from django import forms
from ems_app import models
from bootstrap_datepicker_plus import DatePickerInput

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(format='%d.%m.%Y'), 
            'end_date': DatePickerInput(format='%d.%m.%Y'), 
        }