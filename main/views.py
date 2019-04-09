from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from .forms import main_list_form, UploadFileForm, DateForm, main_list_form_update
from django.forms import formset_factory
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .models import main_list_model, Provider_data, Customer_data, From_data, To_data, Yeruka2_data, Yeruka_data,\
    Status_data, Service_data, Car_data, Driver_data, Flight_data
from django.http import JsonResponse
from itertools import chain
import json
import csv
# from io import StringIO
import io
from django.db import IntegrityError
# import codecs
# https://stackoverflow.com/questions/20926403/heroku-rake-dbmigrate-results-in-error-r13-attach-error-failed-to-attach-t/21148716#21148716
# http://jsfiddle.net/QLfMU/116/
from django_tables2 import RequestConfig
from .tables import main_list_Table
from datetime import datetime, timedelta
from .admin import main_list_Resource
import os
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from .resources import main_list_Resource
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt

BASE_DIR = settings.BASE_DIR


def export_csv(request):
    main_list_resource = main_list_Resource()
    dataset = main_list_resource.export()

    msg = EmailMessage("caneti", 'test csv attachment', to=['aviadm24@gmail.com'])
    msg.attach('test.csv', dataset.csv, 'text/csv')
    msg.content_subtype = "html"
    msg.send()
    # response = HttpResponse(dataset.csv, content_type='text/csv')

    # response['Content-Disposition'] = 'attachment; filename="persons.csv"'

    # return response
    return redirect('/')

def send_backup():
    main_list_resource = main_list_Resource()
    dataset = main_list_resource.export()

    msg = EmailMessage("test backup", 'test backup', to=['aviadm24@gmail.com'])
    msg.attach('test.csv', dataset.csv, 'text/csv')
    msg.content_subtype = "html"
    msg.send()



@csrf_exempt
def export_table(request):
    mainlist = request.POST.get('mainlist')
    print('main list:', type(mainlist))
    sum_list = request.POST.get('sum_list')
    mail = request.POST.get('mail')
    content = render_to_string('main/send_tables.html', {'mainlist': mainlist, 'sum_list': sum_list}, request=request)
    msg = EmailMessage("caneti", content, to=[mail])
    # msg.attach('my_pdf.pdf', pdf, 'application/pdf')
    msg.content_subtype = "html"
    msg.send()

    return render(request, 'main/send_tables.html', {'mainlist': mainlist, 'sum_list': sum_list})



def to_send(request):
    print('to send view')
    field_names = request.session.get('field_names', '')

    # end_filter = request.session.get('end_filter', '')
    return render(request, 'main/to_send.html', {'field_names': field_names}) #, 'end_filter': model.query

def table_view(request):
    table = main_list_Table(main_list_model.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'main/table_view.html', {'table': table})


def main_list(request):
    try:
        now = datetime.now()
        date = now.date()
        backup_date = request.session['back_up_date']
        print('try backup_date: ', datetime.strptime(backup_date, '%Y-%m-%d').date())
        delta = date - datetime.strptime(backup_date, '%Y-%m-%d').date()
        if delta.days > 30:
            print('30 days pased')
            send_backup()
            request.session['back_up_date'] = datetime.strftime(date, '%Y-%m-%d')
    except:
        now = datetime.now()
        date = now.date()
        request.session['back_up_date'] = datetime.strftime(date, '%Y-%m-%d')
        backup_date = request.session['back_up_date']
        print('except backup_date: ', backup_date)

    field_names = [f.name for f in main_list_model._meta.get_fields()]
    now = timezone.now()
    #  https://stackoverflow.com/questions/7503241/django-models-selecting-single-field
    p_num_list = main_list_model.objects.values_list('Project_num', flat=True)
    p_num_set = set(p_num_list)
    # p_num_filterd_list = main_list_model.objects.filter(Date__gte=now).values_list('Project_num', flat=True)
    customer_list = main_list_model.objects.values_list('Customer', flat=True)
    customer_set = set(customer_list)
    # for i in customer_list:
    #     print('customer_list: ', i)
    provider_list = main_list_model.objects.values_list('Provider', flat=True)
    provider_set = set(provider_list)
    last_month = datetime.today() - timedelta(days=30)
    # all = main_list_model.objects.all().order_by('Date')
    # passed = transfer.objects.filter(Date__lt=now).order_by('Date')

    # table_upcoming = main_list_model.objects.filter(Date__gte=last_month).order_by('Date')
    table_upcoming = main_list_Table(main_list_model.objects.filter(Date__gte=last_month).order_by('Date'))
    # table_all = main_list_Table(main_list_model.objects.all())
    RequestConfig(request, paginate=False).configure(table_upcoming)

    if request.method == 'POST':
        print('main list - post')
        form = main_list_form(request.POST)
        date_form = DateForm(request.POST)
        # print('view - from:', request.POST['From'])
        if 'date_filter' in request.POST:
            if date_form.is_valid():
                start = date_form.cleaned_data['start']
                end = date_form.cleaned_data['end']
                table_upcoming = main_list_Table(main_list_model.objects.filter(Date__range=[start, end]))
                return render(request, 'main/main_list_model_form.html', {'form': form,
                                                              'field_names': field_names[1:],
                                                              'table_upcoming': table_upcoming,
                                                              'p_num_list': p_num_set,
                                                              'customer_list': customer_set,
                                                              'provider_list': provider_set,
                                                              'date_form': date_form})
            else:
                print('date form error: ', date_form.errors)
        else:
            if form.is_valid():
                for key, value in form.cleaned_data.items():
                    print(key)
                    if key == 'Flight_num':
                        if Flight_data.objects.filter(Flight=value).exists():
                            pass
                        else:
                            print(value)
                            f = Flight_data.objects.create(Flight=value)
                    if key == 'From':
                        if From_data.objects.filter(From=value).exists():
                            pass
                        else:
                            f = From_data.objects.create(From=value)
                    if key == 'To':
                        if To_data.objects.filter(To=value).exists():
                            pass
                        else:
                            f = To_data.objects.create(To=value)
                # from_changeToDollarSign = form.save(commit=False)
                # from_changeToDollarSign.Cost_per_client = str(form.cleaned_data['Cost_per_client'])+'33'
                # print('Cost_per_client: ', from_changeToDollarSign.Cost_per_client)
                # from_changeToDollarSign.save()
                # change to dollar sign in form clean functions

                form.save()
                messages.success(request, 'Your order was successfully updated!')
                return redirect('main_list')
            else:
                print('main list - got an error: ', form.errors)
                messages.error(request, 'Please correct the error below')

    else:
        form = main_list_form()
        date_form = DateForm()

    return render(request, 'main/main_list_model_form.html', {'form': form,
                                                              'field_names': field_names[1:],
                                                              'table_upcoming': table_upcoming,
                                                              'p_num_list': p_num_set,
                                                              'customer_list': customer_set,
                                                              'provider_list': provider_set,
                                                              'date_form': date_form})

def whole_list(request):

    table_all = main_list_Table(main_list_model.objects.all())
    RequestConfig(request, paginate=False).configure(table_all)

    # field_names = [f.name for f in main_list_model._meta.get_fields()]
    # all = main_list_model.objects.all().order_by('Date')
    # print('all: ', all)
    return render(request, 'main/whole_list.html', {'table_all': table_all})



def add_dollar(request):
    id = request.GET.get('id')
    td_id = request.GET.get('td_id')
    new_int = request.GET.get('new_int')
    data = main_list_model.objects.filter(pk=id)
    print('data: ', data.values())
    td_data = data.values()[0][td_id]
    print('td_data: ', td_data)

    if td_id == 'Extra_KM_client':
        main_list_model.objects.filter(pk=id).update(Extra_KM_client=new_int)
    if td_id == 'Extra_KM_provider':
        main_list_model.objects.filter(pk=id).update(Extra_KM_provider=new_int)
    if td_id == 'Cost_per_client':
        main_list_model.objects.filter(pk=id).update(Cost_per_client=new_int)
    if td_id == 'Cost_per_provider':
        main_list_model.objects.filter(pk=id).update(Cost_per_provider=new_int)
    if td_id == 'Cost_transfer_client':
        main_list_model.objects.filter(pk=id).update(Cost_transfer_client=new_int)

    if td_id == 'Cost_transfer_provider':
        main_list_model.objects.filter(pk=id).update(Cost_transfer_provider=new_int)
    if td_id == 'Cost_extra_hour_client':
        main_list_model.objects.filter(pk=id).update(Cost_extra_hour_client=new_int)
    if td_id == 'Cost_extra_hour_provider':
        main_list_model.objects.filter(pk=id).update(Cost_extra_hour_provider=new_int)
    if td_id == 'Cost_VIP_client':
        main_list_model.objects.filter(pk=id).update(Cost_VIP_client=new_int)
    if td_id == 'Cost_VIP_provider':
        main_list_model.objects.filter(pk=id).update(Cost_VIP_provider=new_int)

    return JsonResponse({})

def add_shekel(request):
    id = request.GET.get('id')
    td_id = request.GET.get('td_id')
    new_int = request.GET.get('new_int')
    data = main_list_model.objects.filter(pk=id)
    print('data: ', data.values())
    td_data = data.values()[0][td_id]
    print('td_data: ', td_data)

    if td_id == 'Extra_KM_client':
        main_list_model.objects.filter(pk=id).update(Extra_KM_client=new_int)
    if td_id == 'Extra_KM_provider':
        main_list_model.objects.filter(pk=id).update(Extra_KM_provider=new_int)
    if td_id == 'Cost_per_client':
        main_list_model.objects.filter(pk=id).update(Cost_per_client=new_int)
    if td_id == 'Cost_per_provider':
        main_list_model.objects.filter(pk=id).update(Cost_per_provider=new_int)
    if td_id == 'Cost_transfer_client':
        main_list_model.objects.filter(pk=id).update(Cost_transfer_client=new_int)

    if td_id == 'Cost_transfer_provider':
        main_list_model.objects.filter(pk=id).update(Cost_transfer_provider=new_int)
    if td_id == 'Cost_extra_hour_client':
        main_list_model.objects.filter(pk=id).update(Cost_extra_hour_client=new_int)
    if td_id == 'Cost_extra_hour_provider':
        main_list_model.objects.filter(pk=id).update(Cost_extra_hour_provider=new_int)
    if td_id == 'Cost_VIP_client':
        main_list_model.objects.filter(pk=id).update(Cost_VIP_client=new_int)
    if td_id == 'Cost_VIP_provider':
        main_list_model.objects.filter(pk=id).update(Cost_VIP_provider=new_int)

    return JsonResponse({})

def add_euro(request):
    id = request.GET.get('id')
    td_id = request.GET.get('td_id')
    new_int = request.GET.get('new_int')
    data = main_list_model.objects.filter(pk=id)
    print('data: ', data.values())
    td_data = data.values()[0][td_id]
    print('td_data: ', td_data)

    if td_id == 'Extra_KM_client':
        main_list_model.objects.filter(pk=id).update(Extra_KM_client=new_int)
    if td_id == 'Extra_KM_provider':
        main_list_model.objects.filter(pk=id).update(Extra_KM_provider=new_int)
    if td_id == 'Cost_per_client':
        main_list_model.objects.filter(pk=id).update(Cost_per_client=new_int)
    if td_id == 'Cost_per_provider':
        main_list_model.objects.filter(pk=id).update(Cost_per_provider=new_int)
    if td_id == 'Cost_transfer_client':
        main_list_model.objects.filter(pk=id).update(Cost_transfer_client=new_int)

    if td_id == 'Cost_transfer_provider':
        main_list_model.objects.filter(pk=id).update(Cost_transfer_provider=new_int)
    if td_id == 'Cost_extra_hour_client':
        main_list_model.objects.filter(pk=id).update(Cost_extra_hour_client=new_int)
    if td_id == 'Cost_extra_hour_provider':
        main_list_model.objects.filter(pk=id).update(Cost_extra_hour_provider=new_int)
    if td_id == 'Cost_VIP_client':
        main_list_model.objects.filter(pk=id).update(Cost_VIP_client=new_int)
    if td_id == 'Cost_VIP_provider':
        main_list_model.objects.filter(pk=id).update(Cost_VIP_provider=new_int)

    return JsonResponse({})


def add_color_json(request):
    color = request.GET.get('color')
    if color == '':
        id = request.GET.get('id')
        td_id = request.GET.get('td_id')
        text_color = request.GET.get('text_color')
        print('text_color: ', text_color)

        data = main_list_model.objects.filter(pk=id)
        color_data = data.values()[0]['Color']
        try:
            color_json_load = json.loads(color_data)
        except TypeError:
            color_json_load = json.loads('{}')
        print('color data: ', type(color_json_load))
        print('color: ', color_json_load)

        if text_color == 'true':
            color_json_load.pop(td_id + '_text', None)
            color_json = json.dumps(color_json_load)
            main_list_model.objects.filter(pk=id).update(Color=color_json)
            print('new text color: ', type(color_json))
        else:
            color_json_load.pop(td_id, None)
            color_json = json.dumps(color_json_load)
            main_list_model.objects.filter(pk=id).update(Color=color_json)
            print('new color: ', type(color_json))

    else:
        id = request.GET.get('id')
        td_id = request.GET.get('td_id')
        text_color = request.GET.get('text_color')
        print('text_color: ', text_color)

        data = main_list_model.objects.filter(pk=id)
        color_data = data.values()[0]['Color']
        try:
            color_json_load = json.loads(color_data)
        except TypeError:
            color_json_load = json.loads('{}')
        print('color data: ', type(color_json_load))
        if color_data == None:
            color_data = {}
        print('color: ', color_json_load)

        if text_color == 'true':
            color_json_load[td_id+'_text'] = color
            color_json = json.dumps(color_json_load)
            main_list_model.objects.filter(pk=id).update(Color=color_json)
            print('new text color: ', type(color_json))
        else:
            color_json_load[td_id] = color
            color_json = json.dumps(color_json_load)
            main_list_model.objects.filter(pk=id).update(Color=color_json)
            print('new color: ', type(color_json))

    return JsonResponse({'is_taken': 'is_taken'})


def update_cell_json(request):
    new_value = request.GET.get('new_value')
    print('new val', new_value)
    if new_value != '':
        id = request.GET.get('id')
        td_id = request.GET.get('td_id')
        print('id val', id)
        td_id = td_id.split()[0]
        print('td_id val', td_id)
        data = main_list_model.objects.filter(pk=id)
        td_id_data = data.values()[0][td_id]

        if td_id == 'Project_num':
            main_list_model.objects.filter(pk=id).update(Project_num=new_value)
        if td_id == 'Customer':
            main_list_model.objects.filter(pk=id).update(Customer=new_value)
        if td_id == 'Contact':
            main_list_model.objects.filter(pk=id).update(Contact=new_value)


        if td_id == 'Date':
            main_list_model.objects.filter(pk=id).update(Date=new_value)
        if td_id == 'Type_of_service':
            main_list_model.objects.filter(pk=id).update(Type_of_service=new_value)
        if td_id == 'Type_of_car':
            main_list_model.objects.filter(pk=id).update(Type_of_car=new_value)
        if td_id == 'Name':
            main_list_model.objects.filter(pk=id).update(Name=new_value)
        if td_id == 'Luggage':
            main_list_model.objects.filter(pk=id).update(Luggage=new_value)

        if td_id == 'Flight_num':
            main_list_model.objects.filter(pk=id).update(Flight_num=new_value)
        if td_id == 'Flight_shcedule':
            main_list_model.objects.filter(pk=id).update(Flight_shcedule=new_value)
        if td_id == 'Start_time':
            main_list_model.objects.filter(pk=id).update(Start_time=new_value)
        if td_id == 'End_time':
            main_list_model.objects.filter(pk=id).update(End_time=new_value)
        if td_id == 'From':
            main_list_model.objects.filter(pk=id).update(From=new_value)
        if td_id == 'To':
            main_list_model.objects.filter(pk=id).update(To=new_value)
        if td_id == 'Provider':
            main_list_model.objects.filter(pk=id).update(Provider=new_value)
        if td_id == 'Driver_name':
            main_list_model.objects.filter(pk=id).update(Driver_name=new_value)
        if td_id == 'status_cheshbonit_yeruka1':
            main_list_model.objects.filter(pk=id).update(status_cheshbonit_yeruka1=new_value)
        if td_id == 'Comments':
            main_list_model.objects.filter(pk=id).update(Comments=new_value)
        if td_id == 'Status':
            main_list_model.objects.filter(pk=id).update(Status=new_value)
        if td_id == 'status_cheshbonit_yeruka2':
            main_list_model.objects.filter(pk=id).update(status_cheshbonit_yeruka2=new_value)

        if td_id == 'Extra_hours_client':
            main_list_model.objects.filter(pk=id).update(Extra_hours_client=new_value)
        if td_id == 'Based_on_client':
            main_list_model.objects.filter(pk=id).update(Based_on_client=new_value)
        if td_id == 'Extra_hours_provider':
            main_list_model.objects.filter(pk=id).update(Extra_hours_provider=new_value)
        if td_id == 'Based_on_provider':
            main_list_model.objects.filter(pk=id).update(Based_on_provider=new_value)

        if td_id == 'KM':
            main_list_model.objects.filter(pk=id).update(KM=new_value)
        if td_id == 'Extra_KM_client':
            main_list_model.objects.filter(pk=id).update(Extra_KM_client=new_value)
        if td_id == 'Extra_KM_provider':
            main_list_model.objects.filter(pk=id).update(Extra_KM_provider=new_value)
        if td_id == 'Cost_per_client':
            main_list_model.objects.filter(pk=id).update(Cost_per_client=new_value)

        if td_id == 'Cost_per_provider':
            main_list_model.objects.filter(pk=id).update(Cost_per_provider=new_value)
        if td_id == 'Cost_transfer_client':
            main_list_model.objects.filter(pk=id).update(Cost_transfer_client=new_value)
        if td_id == 'Cost_transfer_provider':
            main_list_model.objects.filter(pk=id).update(Cost_transfer_provider=new_value)
        if td_id == 'Cost_extra_hour_client':
            main_list_model.objects.filter(pk=id).update(Cost_extra_hour_client=new_value)

        if td_id == 'Cost_extra_hour_provider':
            main_list_model.objects.filter(pk=id).update(Cost_extra_hour_provider=new_value)
        if td_id == 'Cost_VIP_client':
            main_list_model.objects.filter(pk=id).update(Cost_VIP_client=new_value)
        if td_id == 'Cost_VIP_provider':
            main_list_model.objects.filter(pk=id).update(Cost_VIP_provider=new_value)
        if td_id == 'shonot_client':
            main_list_model.objects.filter(pk=id).update(shonot_client=new_value)
        if td_id == 'shonot_provider':
            main_list_model.objects.filter(pk=id).update(shonot_provider=new_value)


    # else:
    #     id = request.GET.get('id')
    #     td_id = request.GET.get('td_id')
    #     text_color = request.GET.get('text_color')
    #     print('text_color: ', text_color)
    #
    #     data = main_list_model.objects.filter(pk=id)
    #     color_data = data.values()[0]['Color']
    #     try:
    #         color_json_load = json.loads(color_data)
    #     except TypeError:
    #         color_json_load = json.loads('{}')
    #     print('color data: ', type(color_json_load))
    #     if color_data == None:
    #         color_data = {}
    #     print('color: ', color_json_load)
    #
    #     if text_color == 'true':
    #         color_json_load[td_id+'_text'] = color
    #         color_json = json.dumps(color_json_load)
    #         main_list_model.objects.filter(pk=id).update(Color=color_json)
    #         print('new text color: ', type(color_json))
    #     else:
    #         color_json_load[td_id] = color
    #         color_json = json.dumps(color_json_load)
    #         main_list_model.objects.filter(pk=id).update(Color=color_json)
    #         print('new color: ', type(color_json))

    return JsonResponse({'is_taken': 'is_taken'})



# def add_color(request):
#     color = request.GET.get('color')
#     if color == '':
#         pass
#     else:
#         id = request.GET.get('id')
#         td_id = request.GET.get('td_id')
#         text_color = request.GET.get('text_color')
#         print('text_color: ', text_color)
#
#         old_color = main_list_model.objects.filter(pk=id)
#         old_color_data = old_color.values()[0]['Color']
#         if old_color_data == None:
#             old_color_data = ''
#         print('old_color: ', old_color_data)
#
#         if text_color == 'true':
#             main_list_model.objects.filter(pk=id).update(Color=old_color_data + td_id + '-' + color + '-' + text_color + '^')
#             print('new text color: ', td_id + '-' + color + '-' + text_color + '^')
#         else:
#             main_list_model.objects.filter(pk=id).update(Color=old_color_data + td_id + '-' + color + '^')
#             print('new color: ', td_id + '-' + color + '-' + '^')
#
#     return JsonResponse({'is_taken': 'is_taken'})

class update(UpdateView):
    model = main_list_model
    form_class = main_list_form_update
    # fields = '__all__'
    success_url = reverse_lazy('main_list')
    template_name_suffix = '_update_form'

    # def form_valid(self, form):
    #   pass

    def get_form_kwargs(self):
        kwargs = super(update, self).get_form_kwargs()

        if 'data' in kwargs.keys():
            print('kwargs: ', kwargs['data'].keys())
            for key in kwargs['data'].keys():
                if key == 'Flight_num':
                    if Flight_data.objects.filter(Flight=kwargs['data'][key]).exists():
                        pass
                    else:
                        print('creat in kwargs: ', kwargs['data'][key])
                        f = Flight_data.objects.create(Flight=kwargs['data'][key])
        return kwargs

    def check_for_null(self, field, model, query_dicy=None):
        if field:
            return model.objects.get(**query_dicy).pk
        else:
            return '-'

    def check_for_null_returns_string(self, field, model, query_dicy=None):
        if field:
            return model.objects.get(**query_dicy)
        else:
            return '-'

    def get_initial(self):
        if self.get_object().Customer != None:
            customer = Customer_data.objects.get(Customer_name=self.get_object().Customer).pk
        else:
            customer = '-'

        driver_field = self.get_object().Driver_name
        driver = self.check_for_null(driver_field, Driver_data, {'Driver': driver_field})

        provider_field = self.get_object().Provider
        provider = self.check_for_null(provider_field, Provider_data, {'Provider_name': provider_field})

        service_data_field = self.get_object().Type_of_service
        service_data = self.check_for_null(service_data_field, Service_data, {'Service': service_data_field})

        status_data_field = self.get_object().Status
        status_data = self.check_for_null(status_data_field, Status_data, {'Status': status_data_field})

        yeruka_data_field = self.get_object().status_cheshbonit_yeruka1
        yeruka_data = self.check_for_null(yeruka_data_field, Yeruka_data, {'Yeruka': yeruka_data_field})

        yeruka2_data_field = self.get_object().status_cheshbonit_yeruka2
        yeruka2_data = self.check_for_null(yeruka2_data_field, Yeruka2_data, {'Yeruka2': yeruka2_data_field})

        to_data_field = self.get_object().To
        to_data = self.check_for_null_returns_string(to_data_field, To_data, {'To': to_data_field})

        from_data_field = self.get_object().From
        from_data = self.check_for_null_returns_string(from_data_field, From_data, {'From': from_data_field})

        car_data_field = self.get_object().Type_of_car
        car_data = self.check_for_null(car_data_field, Car_data, {'Car': car_data_field})

        flight_data_field = self.get_object().Flight_num
        flight_data = self.check_for_null_returns_string(flight_data_field, Flight_data, {'Flight': flight_data_field})
        print('initail flight data: ', flight_data)
        return {
            'Customer': customer,
            'Driver_name': driver,
            'Provider': provider,
            'Type_of_service': service_data,
            'Status': status_data,
            'status_cheshbonit_yeruka1': yeruka_data,
            'status_cheshbonit_yeruka2': yeruka2_data,
            'To': to_data,
            'From': from_data,
            'Type_of_car': car_data,
            'Flight_num': flight_data
        }

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            csvfile = request.FILES['file']
            # dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024).decode('utf-8'))
            # https: // stackoverflow.com / questions / 29663749 / typeerror - cant - use - a - string - pattern - on - a - bytes - like - object - api
            # csvfile.open()
            # reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

            # very important!!!
            # https://andromedayelton.com/2017/04/25/adventures-with-parsing-django-uploaded-csv-files-in-python3/
            csvfile.seek(0)
            # file_reader = csv.DictReader(io.StringIO(csvfile.read().decode('utf-8')))
            if csvfile.name == 'model_data.csv':
                file_reader = csv.reader(io.StringIO(csvfile.read().decode('utf-8')))
                for num, row in enumerate(file_reader):
                    # print('row: ',row)
                    if row[0] == '\ufeffType of service':
                        for data in row[1:]:
                            try:
                                Ser = Service_data()
                                Ser.Service = data
                                Ser.save()
                            except IntegrityError:
                                pass
                    elif row[0] == 'From':
                        for data in row[1:]:
                            try:
                                Fr = From_data()
                                Fr.From = data
                                Fr.save()
                            except IntegrityError:
                                pass
                    elif row[0] == 'To':
                        for data in row[1:]:
                            try:
                                T = To_data()
                                T.To = data
                                T.save()
                            except IntegrityError:
                                pass
                    elif row[0] == 'Yeruka':
                        for data in row[1:]:
                            try:
                                Yer = Yeruka_data()
                                Yer.Yeruka = data
                                Yer.save()
                            except IntegrityError:
                                pass
                    elif row[0] == 'Yeruka2':
                        for data in row[1:]:
                            try:
                                Yer2 = Yeruka2_data()
                                Yer2.Yeruka2 = data
                                Yer2.save()
                            except IntegrityError:
                                pass
                    elif row[0] == 'Status':
                        for data in row[1:]:
                            try:
                                Sta = Status_data()
                                Sta.Status = data
                                Sta.save()
                            except IntegrityError:
                                pass
                    elif row[0] == 'Type of car':
                        for data in row[1:]:
                            try:
                                Ca = Car_data()
                                Ca.Car = data
                                Ca.save()
                            except IntegrityError:
                                pass
            elif csvfile.name == 'csv_data.csv':
                file_reader = csv.DictReader(io.StringIO(csvfile.read().decode('utf-8')))
                for num, row in enumerate(file_reader):
                    if row['\ufeffשם ספק'] != '':
                        print('num: ', num, 'name: ',  row['\ufeffשם ספק'])
                        # try:
                        Provider = Provider_data()
                        print('name: ', row['\ufeffשם ספק'])
                        name = row['\ufeffשם ספק']
                        Provider.Provider_name = name
                        mail = row['כתובות מייל']
                        if mail == '':
                            mail = 'חסר'
                        Provider.email = mail
                        phone = row['טלפון']
                        if phone == '':
                            phone = 'חסר'
                        Provider.phone_num = phone
                        city = row['עיר']
                        if city == '':
                            city = 'חסר'
                        Provider.city = city
                        address = row['כתובת']
                        if address == '':
                            address = 'חסר'
                        Provider.address = address
                        id_num = row['מספר עוסק']
                        if id_num == '':
                            id_num = 'חסר'
                        print('id num: ', id_num)
                        Provider.id_num = id_num
                        contact = row['שם איש קשר']
                        if contact == '':
                            contact = 'חסר'
                        Provider.contact = contact
                        used_a_lot = row['ספק']
                        if used_a_lot == 'סס':
                            Provider.used_a_lot = True
                        Provider.save()
                        # except IntegrityError:
                        #     print('row: ', row)
                        #     print('IntegrityError: ', row['\ufeffשם ספק'])
            else:
                print('file name: ', csvfile.name)
                file_reader = csv.DictReader(io.StringIO(csvfile.read().decode('utf-8')))
                for num, row in enumerate(file_reader):
                    print('row: ', num)
                    if row['\ufeffשם לקוח'] != '':
                        try:
                            Customer = Customer_data()
                            # print('name: ', row['\ufeffשם לקוח'])
                            name = row['\ufeffשם לקוח']
                            if '"' in name:
                                print('bad name: ', name)
                                name = '-'.join(name.split('"'))
                            Customer.Customer_name = name
                            mail = row['כתובות מייל']
                            if mail == '':
                                mail = 'חסר'
                            Customer.email = mail
                            phone = row['טלפון']
                            if phone == '':
                                phone = 'חסר'
                            Customer.phone_num = phone
                            city = row['עיר']
                            if city == '':
                                city = 'חסר'
                            Customer.city = city
                            address = row['כתובת']
                            if address == '':
                                address = 'חסר'
                            Customer.address = address
                            id_num = row['מספר עוסק']
                            if id_num == '':
                                id_num = 'חסר'
                            print('id num: ', id_num)
                            Customer.id_num = id_num
                            contact = row['שם איש קשר']
                            if contact == '':
                                contact = 'חסר'
                            Customer.contact = contact
                            used_a_lot = row['לקוח']
                            if used_a_lot == 'לל':
                                Customer.used_a_lot = True
                            Customer.save()
                        except IntegrityError:
                            print('IntegrityError: ', row['\ufeffשם לקוח'])
            # data = file_reader[0]

            # file_reader = csv.reader(csvfile, delimiter=',')
            # for row in file_reader:
            #     print(row)


            return render(request, 'main/upload.html', locals())
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})

# def update_row(request):
#     if request.method == 'POST':
#         print('update_row - view')
#         form = main_list_form(request.POST)
#         if form.is_valid():
#             print('form pk:', form.pk)
#             form.save()
#             messages.success(request, ('Your order was successfully updated!'))
#             return redirect('add_main_list')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     return render(request, 'main/main_list_model_form.html')
