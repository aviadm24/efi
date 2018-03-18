from .models import transfer, project, Model_data, Car_data, Provider_data\
                    , Driver_data, Customer_ref_data, Proj
from django import forms
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from bootstrap_datepicker.widgets import DatePicker

# class new_project_form(forms.ModelForm):
#     class Meta:
#         model = Proj
#         fields = '__all__'


class project_form(forms.ModelForm):
    # Start_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))
    # End_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))
    class Meta:
        model = project
        fields = ['Date', 'Name', 'Type_of_car', 'Type_of_service', 'Driver', 'Provider', 'Flight',
                  'Based_on', 'Start_time', 'End_time', 'Extra_hours', 'KM', 'Extra_KM']

    def __init__(self, *args, **kwargs):
        super(project_form, self).__init__(*args, **kwargs)
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'})
        self.fields['Based_on'].widget = forms.TimeInput(attrs={'id': 'timepicker1'})
        # self.fields['End_time'].widget = forms.TimeInput(attrs={'id': 'timepicker1'})
        self.fields['KM'].widget = forms.NumberInput(
            attrs={'type': "number", 'min': 10, 'max': 500, 'step': "1", 'placeholder': "50"})


# https://stackoverflow.com/questions/17492374/how-to-render-formset-in-template-django-and-create-vertical-table
class transfer_form(forms.ModelForm):
    # Date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    Customer_ref = forms.ModelChoiceField(queryset=Customer_ref_data.objects.all())
    Driver = forms.ModelChoiceField(queryset=Driver_data.objects.all())
    Car = forms.ModelChoiceField(queryset=Car_data.objects.all())
    Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all())
    Model = forms.ModelChoiceField(queryset=Model_data.objects.all())

    class Meta:
        model = transfer
        fields = ['Customer_ref', 'Driver', 'Provider', 'Car', 'Model', 'Clients_Name',
                  'Service_from_to', 'Flight', 'Time_from_to', 'Contact', 'Date']

    def __init__(self, *args, **kwargs):
        super(transfer_form, self).__init__(*args, **kwargs)
        CHOICES1 = (
            ('yes', 'כן'),
            ('no', 'לא'),
        )

        # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'})
        # self.fields['Flight'].widget = forms.Select(choices=CHOICES1)


