from .models import transfer, project, formData
from django import forms
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from bootstrap_datepicker.widgets import DatePicker

class form_data_Customer_ref(forms.ModelForm):
    class Meta:
        model = formData
        exclude = ['Driver', 'Provider', 'Car', 'Model',]


class project_form(forms.ModelForm):
    class Meta:
        model = project
        fields = ['Date', 'Name', 'Type_of_car', 'Type_of_service', 'Driver', 'Provider', 'Flight',
                  'Based_on', 'Start_time', 'End_time', 'Extra_hours', 'KM', 'Extra_KM']

    def __init__(self, *args, **kwargs):
        super(project_form, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_intake_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('received_by', 'client_first_name', 'client_last_name', css_class='col-md-6'),
                Div('status', 'notes', css_class='col-md-6'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'Save'), css_class='col-md-12'), css_class='row'
            )
        )
# https://stackoverflow.com/questions/17492374/how-to-render-formset-in-template-django-and-create-vertical-table
class transfer_form(forms.ModelForm):
    Customer_ref = forms.ModelChoiceField(queryset=formData.objects.all())
    Date = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )

    class Meta:
        model = transfer
        fields = ['Customer_ref', 'Date', 'Driver', 'Provider', 'Car', 'Clients_Name',
                  'Service_from_to', 'Flight', 'Time_from_to', 'KM', 'Contact', 'Project']

    def __init__(self, *args, **kwargs):
        super(transfer_form, self).__init__(*args, **kwargs)
        CHOICES1 = (
            ('yes', 'כן'),
            ('no', 'לא'),
        )
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                'Customer_ref', 'Date', 'Driver', css_class="form-row"
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

        # self.fields['Date'].widget = forms.DateInput(
        #     attrs={'placeholder': "2009-10-03"})
        # self.fields['Driver'].widget = forms.Select(choices=CHOICES1)
        # self.fields['Provider'].widget = forms.Select(choices=CHOICES1)
        # self.fields['Car'].widget = forms.Select(choices=CHOICES1)
        # self.fields['Flight'].widget = forms.Select(choices=CHOICES1)

        self.fields['KM'].widget = forms.NumberInput(
            attrs={'type': "number", 'min': 10, 'max': 500, 'step': "1", 'placeholder': "50"})

