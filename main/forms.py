from .models import transfer, project, Model_data, Car_data, Provider_data\
                    , Driver_data, Customer_data, Proj, main_list_model
from django import forms
from .utils import OptionalChoiceField
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

class main_list_form(forms.ModelForm):
    class Meta:
        model = main_list_model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(main_list_form, self).__init__(*args, **kwargs)
        # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'})


class project_form(forms.ModelForm):
    Driver = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
    Type_of_car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
    Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)

    class Meta:
        model = project
        fields = ['Date', 'Name', 'Type_of_car', 'Type_of_service', 'Driver', 'Provider', 'Flight',
                  'Based_on', 'Start_time', 'End_time', 'Extra_hours', 'KM', 'Extra_KM']

    # def __init__(self, *args, **kwargs):
    #     super(project_form, self).__init__(*args, **kwargs)
    #
    #     # class ="form-control datetimepicker-input" data-target="#datetimepicker1"
    #     self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'})
    #     self.fields['Based_on'].widget = forms.TimeInput(attrs={'id': 'timepicker1'})
    #     # self.fields['End_time'].widget = forms.TimeInput(attrs={'id': 'timepicker1'})
    #     self.fields['KM'].widget = forms.NumberInput(
    #         attrs={'type': "number", 'min': 10, 'max': 500, 'step': "1", 'placeholder': "50"})


# https://stackoverflow.com/questions/17492374/how-to-render-formset-in-template-django-and-create-vertical-table
class transfer_form(forms.ModelForm):
    # print('customer data: ', Customer_data.objects.all().values())
    # OptionalChoiceField(choices=(("", "-----"), ("1", "1"), ("2", "2")))
    # https://stackoverflow.com/questions/24783275/django-form-with-choices-but-also-with-freetext-option


    Driver = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
    Car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
    Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)
    Model = forms.ModelChoiceField(queryset=Model_data.objects.all(), required=False)
    Clients_Name = forms.CharField(required=True)

    class Meta:
        model = transfer
        fields = ['Customer_ref', 'Date', 'Clients_Name', 'Driver', 'Provider', 'Car', 'Model',
                  'From', 'To', 'DepOrArr', 'Flight', 'Time_of_flight', 'Time_of_PU', 'Contact']

    def __init__(self, *args, **kwargs):
        super(transfer_form, self).__init__(*args, **kwargs)
        CHOICES1 = (
            ('yes', 'כן'),
            ('no', 'לא'),
        )

        # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'})
        # self.fields['Flight'].widget = forms.Select(choices=CHOICES1)


