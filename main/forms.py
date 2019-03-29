from .models import Service_data, Car_data, Provider_data,\
    Driver_data, Customer_data, Flight_data, main_list_model, Status_data, Yeruka_data, Yeruka2_data, To_data, From_data
from django import forms
# from django_select2.forms import ModelSelect2Widget, Select2MultipleWidget, Select2Widget
from .utils import OptionalChoiceField
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
# how to use helper crispy forms
# https://stackoverflow.com/questions/18680063/change-input-types-and-attributes-for-a-form-used-in-a-createview-and-updatevi


class DateForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()

class UploadFileForm(forms.Form):
    file = forms.FileField()


class main_list_form(forms.ModelForm):
    Project_num = forms.IntegerField(required=True)
    Customer = forms.ModelChoiceField(queryset=Customer_data.objects.all(), required=False)
    Type_of_service = forms.ModelChoiceField(queryset=Service_data.objects.all(), required=False)
    Type_of_car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
    Driver_name = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
    Flight_shcedule = forms.TimeField()
    Flight_num = forms.CharField(widget=forms.Select(), required=False, initial='')
    Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)
    Status = forms.ModelChoiceField(queryset=Status_data.objects.all(), required=False)
    status_cheshbonit_yeruka1 = forms.ModelChoiceField(queryset=Yeruka_data.objects.all(), required=False)
    status_cheshbonit_yeruka2 = forms.ModelChoiceField(queryset=Yeruka2_data.objects.all(), required=False)
    # To = forms.ModelChoiceField(queryset=To_data.objects.all(), required=False)
    # To = forms.CharField(widget=forms.Select(choices=[(doc, doc) for doc in To_data.objects.all()]), required=False)

    To = forms.CharField(widget=forms.Select(), required=False)

    # From = forms.ModelChoiceField(queryset=From_data.objects.all(), required=False)

    # From = forms.ChoiceField(choices=[(doc, doc) for doc in From_data.objects.all()], required=False)
    # https://stackoverflow.com/questions/5281195/forms-modelchoicefield-queryset-extra-choice-fields-django-forms

    From = forms.CharField(widget=forms.Select(), required=False)

    # From = forms.CharField(widget=forms.Select(choices=[(doc, doc) for doc in From_data.objects.all()]), required=False)
    # https://stackoverflow.com/questions/19770534/django-forms-choicefield-without-validation-of-selected-value

    # https://djangosnippets.org/snippets/200/

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
        self.fields['Cost_per_client'].label = 'מחיר FD ללקוח'
        self.fields['Cost_per_provider'].label = 'מחיר FD לספק'
        self.fields['Cost_extra_hour_client'].label = 'מחיר שעה נוספת ללקוח'
        self.fields['Cost_extra_hour_provider'].label = 'מחיר שעה נוספת לספק'
        self.fields['Cost_transfer_client'].label = 'מחיר טרנספר ללקוח'
        self.fields['Cost_transfer_provider'].label = 'מחיר טרנספר לספק'
        self.fields['Cost_VIP_client'].label = 'מחיר VIP ללקוח'
        self.fields['Cost_VIP_provider'].label = 'מחיר VIP לספק'

        self.fields['shonot_client'].label = 'מחיר שונות ללקוח'
        self.fields['shonot_provider'].label = 'מחיר שונות לספק'

        self.fields['status_cheshbonit_yeruka1'].label = 'סטטוס חשבונית ירוקה - ספק'
        self.fields['status_cheshbonit_yeruka2'].label = 'סטטוס חשבונית ירוקה - לקוח'
        # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
        self.fields['Project_num'].widget.attrs.update({'style': 'width:100px'})
        # self.fields['Flight_shcedule'].widget.attrs.update({'style': 'bgcolor:gray'})
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'}, format='%A, %B %d %Y')

        self.fields['Based_on_client'].widget.attrs.update({'value': '9'})
        self.fields['Based_on_provider'].widget.attrs.update({'value': '10'})

        self.fields['Cost_per_client'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['Cost_per_provider'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['Cost_extra_hour_client'].widget.attrs.update({'value': '50', 'class': 'currency_sign'})
        self.fields['Cost_extra_hour_provider'].widget.attrs.update({'value': '60', 'class': 'currency_sign'})
        self.fields['Cost_transfer_client'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['Cost_transfer_provider'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['Cost_VIP_client'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['Cost_VIP_provider'].widget.attrs.update({'class': 'currency_sign'})

        self.fields['shonot_client'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['shonot_provider'].widget.attrs.update({'class': 'currency_sign'})


        self.fields['From'].widget.attrs.update({'class': 'form-control'})
        self.fields['To'].widget.attrs.update({'class': 'js_tags'})
        self.fields['Flight_num'].widget.attrs.update({'class': 'form-control'})
        self.fields['Flight_num'].widget.choices = [(doc, doc) for doc in Flight_data.objects.all()]
        self.fields['From'].widget.choices = [(doc, doc) for doc in From_data.objects.all()]
        self.fields['To'].widget.choices = [(doc, doc) for doc in To_data.objects.all()]
        # print('choices= ', [(doc, doc) for doc in To_data.objects.all()])
        # self.fields['Color'].widget.attrs.update({'class': 'color'})

    def clean_Cost_per_client(self):
        if self.data['Cost_per_client']:
            return str(self.data['Cost_per_client'])+'33'

    def clean_Cost_per_provider(self):
        if self.data['Cost_per_provider']:
            return str(self.data['Cost_per_provider'])+'33'

    def clean_Cost_transfer_client(self):
        if self.data['Cost_transfer_client']:
            return str(self.data['Cost_transfer_client'])+'33'

    def clean_Cost_transfer_provider(self):
        if self.data['Cost_transfer_provider']:
            return str(self.data['Cost_transfer_provider'])+'33'

    def clean_Cost_extra_hour_client(self):
        if self.data['Cost_extra_hour_client']:
            return str(self.data['Cost_extra_hour_client'])+'33'

    def clean_Cost_extra_hour_provider(self):
        if self.data['Cost_extra_hour_provider']:
            return str(self.data['Cost_extra_hour_provider'])+'33'

    def clean_Cost_VIP_client(self):
        if self.data['Cost_VIP_client']:
            return str(self.data['Cost_VIP_client'])+'33'

    def clean_Cost_VIP_provider(self):
        if self.data['Cost_VIP_provider']:
            return str(self.data['Cost_VIP_provider'])+'33'

    def clean_shonot_client(self):
        if self.data['shonot_client']:
            return str(self.data['shonot_client'])+'33'

    def clean_shonot_provider(self):
        if self.data['shonot_provider']:
            return str(self.data['shonot_provider'])+'33'



    # def clean(self):
    #     cleaned_data = super().clean()
    #     data = cleaned_data.get('From')
    #     print('form data###: ', data)
    #     if data == None:
    #         raise forms.ValidationError('foo')
    #     return cleaned_data

class main_list_form_update(forms.ModelForm):
    Customer = forms.ModelChoiceField(queryset=Customer_data.objects.all(), required=False)
    Type_of_service = forms.ModelChoiceField(queryset=Service_data.objects.all(), required=False)
    Type_of_car = forms.ModelChoiceField(queryset=Car_data.objects.all(), required=False)
    Driver_name = forms.ModelChoiceField(queryset=Driver_data.objects.all(), required=False)
    # Flight_num = forms.ModelChoiceField(queryset=Flight_data.objects.all(), required=False)
    Flight_num = forms.CharField(widget=forms.Select(), required=False)
    Provider = forms.ModelChoiceField(queryset=Provider_data.objects.all(), required=False)
    Status = forms.ModelChoiceField(queryset=Status_data.objects.all(), required=False)
    status_cheshbonit_yeruka1 = forms.ModelChoiceField(queryset=Yeruka_data.objects.all(), required=False)
    status_cheshbonit_yeruka2 = forms.ModelChoiceField(queryset=Yeruka2_data.objects.all(), required=False)
    # To = forms.ModelChoiceField(queryset=To_data.objects.all(), required=False)
    # To = forms.CharField(widget=forms.Select(choices=[(doc, doc) for doc in To_data.objects.all()]), required=False)

    To = forms.CharField(widget=forms.Select(), required=False)

    # From = forms.ModelMultipleChoiceField(queryset=From_data.objects.all(), required=False, widget=Select2MultipleWidget(queryset=From_data.objects.all()))

    # From = forms.ChoiceField(choices=[(doc, doc) for doc in From_data.objects.all()], required=False)
    # https://stackoverflow.com/questions/5281195/forms-modelchoicefield-queryset-extra-choice-fields-django-forms

    From = forms.CharField(widget=forms.Select(), required=False)

    # From = forms.CharField(widget=forms.Select(choices=[(doc, doc) for doc in From_data.objects.all()]), required=False)
    # https://stackoverflow.com/questions/19770534/django-forms-choicefield-without-validation-of-selected-value

    # https://djangosnippets.org/snippets/200/

    def clean_Flight_num(self):
        print('clean Flight_num method')
        print('clean function: ', self.data['Flight_num'])
        if Flight_data.objects.filter(Flight=self.data['Flight_num']).exists():
            pass
        else:
            print('creating: ', self.data['Flight_num'])
            f = Flight_data.objects.create(Flight=self.data['Flight_num'])
        return self.data['Flight_num']

    class Meta:
        model = main_list_model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(main_list_form_update, self).__init__(*args, **kwargs)
        # self.fields['Project_num'].label = 'Project Number'
        self.fields['Customer'].label = 'Refernce custumer'
        self.fields['Customer'].widget.attrs.update({'class': 'js_tags'})
        self.fields['Luggage'].label = 'Number of PAX & Luggage'
        # self.fields['Start_time'].label = 'Start_time'
        self.fields['Cost_per_client'].label = 'מחיר FD ללקוח'
        self.fields['Cost_per_provider'].label = 'מחיר FD לספק'
        self.fields['Cost_extra_hour_client'].label = 'מחיר שעה נוספת ללקוח'
        self.fields['Cost_extra_hour_provider'].label = 'מחיר שעה נוספת לספק'
        self.fields['Cost_transfer_client'].label = 'מחיר טרנספר ללקוח'
        self.fields['Cost_transfer_provider'].label = 'מחיר טרנספר לספק'
        self.fields['Cost_VIP_client'].label = 'מחיר VIP ללקוח'
        self.fields['Cost_VIP_provider'].label = 'מחיר VIP לספק'

        self.fields['shonot_client'].label = 'מחיר שונות ללקוח'
        self.fields['shonot_provider'].label = 'מחיר שונות לספק'

        self.fields['status_cheshbonit_yeruka1'].label = 'סטטוס חשבונית ירוקה - ספק'
        self.fields['status_cheshbonit_yeruka2'].label = 'סטטוס חשבונית ירוקה - לקוח'
        # https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
        self.fields['Project_num'].widget.attrs.update({'style': 'width:100px'})
        self.fields['Date'].widget = forms.DateInput(attrs={'id': 'datepicker1'}, format='%A, %B %d %Y')

        self.fields['Based_on_client'].widget.attrs.update({'value': '9'})
        self.fields['Based_on_provider'].widget.attrs.update({'value': '10'})

        self.fields['Cost_per_client'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        # self.fields['Cost_per_client'].widget.attrs.update({'class': 'currency_sign'})
        self.fields['Cost_per_provider'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['Cost_extra_hour_client'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['Cost_extra_hour_provider'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['Cost_transfer_client'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['Cost_transfer_provider'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['Cost_VIP_client'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['Cost_VIP_provider'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['shonot_client'].widget = forms.TextInput(attrs={'class': 'currency_sign'})
        self.fields['shonot_provider'].widget = forms.TextInput(attrs={'class': 'currency_sign'})

        self.fields['From'].widget.attrs.update({'class': 'form-control'})
        self.fields['To'].widget.attrs.update({'class': 'form-control'})
        # self.fields['Color'].widget.attrs.update(attrs={'display': 'none'})
        self.fields['Flight_num'].widget.choices = [(doc, doc) for doc in Flight_data.objects.all()]
        self.fields['From'].widget.choices = [(doc, doc) for doc in From_data.objects.all()]
        self.fields['To'].widget.choices = [(doc, doc) for doc in To_data.objects.all()]
        # print('choices= ', [(doc, doc) for doc in To_data.objects.all()])