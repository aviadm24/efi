from .models import Service_data, Car_data, Provider_data,\
    Driver_data, Customer_data, Flight_data, main_list_model, Status_data, Yeruka_data, Yeruka2_data
from django import forms
from .utils import OptionalChoiceField
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
# how to use helper crispy forms
# https://stackoverflow.com/questions/18680063/change-input-types-and-attributes-for-a-form-used-in-a-createview-and-updatevi


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


class main_list_form(forms.ModelForm):
    Customer = forms.ModelChoiceField(queryset=Customer_data.objects.all(), required=False)
    Type_of_service = forms.ModelChoiceField(queryset=Service_data.objects.all(), required=False)
    Type_of_car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
    Driver_name = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
    Flight_num = forms.ModelChoiceField(queryset=Flight_data.objects.all(), required=False)
    Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)
    Status = forms.ModelChoiceField(queryset=Status_data.objects.all(), required=False)
    status_cheshbonit_yeruka1 = forms.ModelChoiceField(queryset=Yeruka_data.objects.all(), required=False)
    status_cheshbonit_yeruka2 = forms.ModelChoiceField(queryset=Yeruka2_data.objects.all(), required=False)

    class Meta:
        model = main_list_model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(main_list_form, self).__init__(*args, **kwargs)
        # self.fields['Project_num'].label = 'Project Number'
        self.fields['Customer'].label = 'Refernce custumer'
        self.fields['Customer'].widget.attrs.update({'class': 'js_tags'})
        self.fields['Luggage'].label = 'Number of PAX & Luggage'
        # self.fields['Start_time'].label = 'Start_time'
        self.fields['Cost_per_client'].label = 'מחיר ללקוח'
        self.fields['Cost_per_provider'].label = 'מחיר לספק'
        self.fields['Cost_extra_hour_client'].label = 'מחיר שעה נוספת ללקוח'
        self.fields['Cost_extra_hour_provider'].label = 'מחיר שעה נוספת לספק'
        self.fields['Cost_transfer_client'].label = 'מחיר טרנספר ללקוח'
        self.fields['Cost_transfer_provider'].label = 'מחיר טרנספר לספק'
        self.fields['Cost_VIP_client'].label = 'מחיר VIP ללקוח'
        self.fields['Cost_VIP_provider'].label = 'מחיר VIP לספק'
        # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
        self.fields['Project_num'].widget.attrs.update({'style': 'width:100px'})
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'}, format='%A, %B %d %Y')
        self.fields['Based_on_client'].widget.attrs.update({'value': '9'})
        self.fields['Based_on_provider'].widget.attrs.update({'value': '10'})
        self.fields['Cost_extra_hour_client'].widget.attrs.update({'value': '50'})
        self.fields['Cost_extra_hour_provider'].widget.attrs.update({'value': '60'})
        # self.fields['Color'].widget.attrs.update(attrs={'display': 'none'})


# class project_form(forms.ModelForm):
#     Driver = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
#     Type_of_car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
#     Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)
#
#     class Meta:
#         model = project
#         fields = ['Date', 'Name', 'Type_of_car', 'Type_of_service', 'Driver', 'Provider', 'Flight',
#                   'Based_on', 'Start_time', 'End_time', 'Extra_hours', 'KM', 'Extra_KM']

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
# class transfer_form(forms.ModelForm):
#     # print('customer data: ', Customer_data.objects.all().values())
#     # OptionalChoiceField(choices=(("", "-----"), ("1", "1"), ("2", "2")))
#     # https://stackoverflow.com/questions/24783275/django-form-with-choices-but-also-with-freetext-option
#
#
#     Driver = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
#     Car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
#     Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)
#     # Model = forms.ModelChoiceField(queryset=Model_data.objects.all(), required=False)
#     # Clients_Name = forms.CharField(queryset=Customer_data.objects.all(), required=True)
#
#     class Meta:
#         model = transfer
#         fields = ['Customer_ref', 'Date', 'Clients_Name', 'Driver', 'Provider', 'Car', 'Model',
#                   'From', 'To', 'DepOrArr', 'Flight', 'Time_of_flight', 'Time_of_PU', 'Contact']
#
#     def __init__(self, *args, **kwargs):
#         super(transfer_form, self).__init__(*args, **kwargs)
#         CHOICES1 = (
#             ('yes', 'כן'),
#             ('no', 'לא'),
#         )
#
#         # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
#         self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'})
#         # self.fields['Flight'].widget = forms.Select(choices=CHOICES1)


