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


def export_filter(request):
    # attach a csv to mail
    # https://stackoverflow.com/questions/17584550/attach-generated-csv-file-to-email-and-send-with-django
    project_num = request.GET.get('project_num')
    customer = request.GET.get('customer')
    provider = request.GET.get('provider')
    min = request.GET.get('min')
    max = request.GET.get('max')
    mail = request.GET.get('mail')
    customer_bool = True
    provider_bool = True
    end_filter = None
    if project_num != '---SELECT---':
        print('proj num:', project_num)
        project_filter = main_list_model.objects.filter(Project_num=project_num)
        if customer != '---SELECT---':
            customer_filter = project_filter.objects.filter(Customer=customer)

            provider_bool = False
            if min != '':
                min_filter = customer_filter.objects.filter(Date__gte=min)
                if max != '':
                    end_filter = min_filter.objects.filter(Date__lte=max)
                else:
                    end_filter = min_filter
            else:
                end_filter = customer_filter

        elif provider != '---SELECT---':
            provider_filter = project_filter.objects.filter(Provider=provider)
            customer_bool = False
            if min != '':
                min_filter = provider_filter.objects.filter(Date__gte=min)
                if max != '':
                    end_filter = min_filter.objects.filter(Date__lte=max)
                else:
                    end_filter = min_filter
            else:
                end_filter = provider_filter

        else:
            print('proj num2:', project_num)
            if min != '':
                min_filter = project_filter.objects.filter(Date__gte=min)
                if max != '':
                    end_filter = min_filter.objects.filter(Date__lte=max)
                else:
                    end_filter = min_filter
            else:
                end_filter = project_filter
                table = main_list_Table(main_list_model.objects.filter(Project_num=project_num))
                print('proj num3:', end_filter)
                # return redirect('main/to_send.html', {'end_filter': end_filter})
    else:
        if customer != '---SELECT---':
            provider_bool = False
            print('proj customer_filter:', customer)
            customer_filter = main_list_model.objects.filter(Customer=customer)
            if min != '':
                min_filter = customer_filter.objects.filter(Date__gte=min)
                if max != '':
                    end_filter = min_filter.objects.filter(Date__lte=max)
                else:
                    end_filter = min_filter
            else:
                end_filter = customer_filter
        elif provider != '---SELECT---':
            customer_bool = False
            provider_filter = main_list_model.objects.filter(Provider=provider)
            if min != '':
                min_filter = provider_filter.objects.filter(Date__gte=min)
                if max != '':
                    end_filter = min_filter.objects.filter(Date__lte=max)
                else:
                    end_filter = min_filter
            else:
                end_filter = provider_filter
    # https://stackoverflow.com/questions/43592783/django-template-context-processors-request-issue-with-django-tables2-and-djang
    field_names = [f.name for f in main_list_model._meta.get_fields()]
    field_names.remove('Color')
    # filterd_field_names = []
    if provider_bool == False:
        field_names.remove('Based_on_provider')
        for name in field_names:
            if 'provider' in name:
                field_names.remove(name)
    if customer_bool == False:
        field_names.remove('Based_on_client')
        for name in field_names:
            if 'client' in name:
                field_names.remove(name)
    # print(end_filter)
    # print('field_names: ,', field_names)

    if provider_bool == False:
        end_filter = end_filter.values(*field_names)
        sum_dict = {}
        Cost_extra_hour_client_d = 0
        Cost_extra_hour_client_s = 0
        Cost_extra_hour_client_u = 0

        Cost_per_client_d = 0
        Cost_per_client_s = 0
        Cost_per_client_u = 0

        Cost_transfer_client_d = 0
        Cost_transfer_client_s = 0
        Cost_transfer_client_u = 0

        Cost_VIP_client_d = 0
        Cost_VIP_client_s = 0
        Cost_VIP_client_u = 0

        sum_d = 0
        sum_s = 0
        sum_u = 0

        for data in end_filter:
            print('data:', data)
            if data['Extra_hours_client']: #  > 0
                if data['Cost_extra_hour_client'] % 100 == 33:
                    sum = (data['Cost_extra_hour_client'] // 100) * data['Extra_hours_client']
                    Cost_extra_hour_client_d += sum
                    sum_d += sum
                if data['Cost_extra_hour_client'] % 100 == 34:
                    sum = (data['Cost_extra_hour_client'] // 100) * data['Extra_hours_client']
                    Cost_extra_hour_client_s += sum
                    sum_s += sum
                if data['Cost_extra_hour_client'] % 100 == 35:
                    sum = (data['Cost_extra_hour_client'] // 100) * data['Extra_hours_client']
                    Cost_extra_hour_client_u += sum
                    sum_u += sum

            if data['Cost_per_client']:
                sum = (data['Cost_per_client'] // 100)
                if data['Cost_per_client'] % 100 == 33:
                    Cost_per_client_d += sum
                    sum_d += sum
                if data['Cost_per_client'] % 100 == 34:
                    Cost_per_client_s += sum
                    sum_s += sum
                if data['Cost_per_client'] % 100 == 35:
                    Cost_per_client_u += sum
                    sum_u += sum

            if data['Cost_transfer_client']:
                sum = (data['Cost_transfer_client'] // 100)
                if data['Cost_transfer_client'] % 100 == 33:
                    Cost_transfer_client_d += sum
                    sum_d += sum
                if data['Cost_transfer_client'] % 100 == 34:
                    Cost_transfer_client_s += sum
                    sum_s += sum
                if data['Cost_transfer_client'] % 100 == 35:
                    Cost_transfer_client_u += sum
                    sum_u += sum

            if data['Cost_VIP_client']:
                sum = (data['Cost_VIP_client'] // 100)
                if data['Cost_VIP_client'] % 100 == 33:
                    Cost_VIP_client_d += sum
                    sum_d += sum
                if data['Cost_VIP_client'] % 100 == 34:
                    Cost_VIP_client_s += sum
                    sum_s += sum
                if data['Cost_VIP_client'] % 100 == 35:
                    Cost_VIP_client_u += sum
                    sum_u += sum

            # for i in l:
            #     print('i: ',i)
            #     if data[i] > 0:
            #         sum = (data[i] // 100)
            #         if data[i] % 100 == 33:
            #             b = sum_dict[i+'_d']
            #             b += sum
            #             sum_dict[i + '_d'] = b
            #         if data[i] % 100 == 34:
            #             b = sum_dict[i + '_s']
            #             b += sum
            #             sum_dict[i + '_s'] = b
            #         if data[i] % 100 == 35:
            #             b = sum_dict[i + '_u']
            #             b += sum
            #             sum_dict[i + '_u'] = b

            sum_dict['Cost_extra_hour_client_d'] = Cost_extra_hour_client_d
            sum_dict['Cost_extra_hour_client_s'] = Cost_extra_hour_client_s
            sum_dict['Cost_extra_hour_client_u'] = Cost_extra_hour_client_u

            sum_dict['Cost_per_client_d'] = Cost_per_client_d
            sum_dict['Cost_per_client_s'] = Cost_per_client_s
            sum_dict['Cost_per_client_u'] = Cost_per_client_u

            sum_dict['Cost_transfer_client_d'] = Cost_transfer_client_d
            sum_dict['Cost_transfer_client_s'] = Cost_transfer_client_s
            sum_dict['Cost_transfer_client_u'] = Cost_transfer_client_u

            sum_dict['Cost_VIP_client_d'] = Cost_VIP_client_d
            sum_dict['Cost_VIP_client_s'] = Cost_VIP_client_s
            sum_dict['Cost_VIP_client_u'] = Cost_VIP_client_u

            sum_dict['sum_d'] = sum_d
            sum_dict['sum_s'] = sum_s
            sum_dict['sum_u'] = sum_u

            sum_dict['sum_d_m'] = sum_d*1.17
            sum_dict['sum_s_m'] = sum_s*1.17
            sum_dict['sum_u_m'] = sum_u*1.17
        print('sum dict: ', sum_dict)
        sum_table_fields = ['Cost_per_client', 'Extra_hours_client', 'Cost_transfer_client', 'Cost_VIP_client', 'sum', 'sum+maam']



        # extra_hours_client = end_filter.objects.values_list('Extra_hours_client', flat=True)

    if customer_bool == False:
        end_filter = end_filter.values(*field_names)
        sum_dict = {}
        Cost_extra_hour_provider_d = 0
        Cost_extra_hour_provider_s = 0
        Cost_extra_hour_provider_u = 0

        Cost_per_provider_d = 0
        Cost_per_provider_s = 0
        Cost_per_provider_u = 0

        Cost_transfer_provider_d = 0
        Cost_transfer_provider_s = 0
        Cost_transfer_provider_u = 0

        Cost_VIP_provider_d = 0
        Cost_VIP_provider_s = 0
        Cost_VIP_provider_u = 0

        sum_d = 0
        sum_s = 0
        sum_u = 0

        for data in end_filter:
            if data['Extra_hours_provider']:  # > 0:
                sum = (data['Cost_extra_hour_provider'] // 100) * data['Extra_hours_provider']
                if data['Cost_extra_hour_provider'] % 100 == 33:
                    Cost_extra_hour_provider_d += sum
                    sum_d += sum
                if data['Cost_extra_hour_provider'] % 100 == 34:
                    Cost_extra_hour_provider_s += sum
                    sum_s += sum
                if data['Cost_extra_hour_provider'] % 100 == 35:
                    Cost_extra_hour_provider_u += sum
                    sum_u += sum

            if data['Cost_per_provider']:
                sum = (data['Cost_per_provider'] // 100)
                if data['Cost_per_provider'] % 100 == 33:
                    Cost_per_provider_d += sum
                    sum_d += sum
                if data['Cost_per_provider'] % 100 == 34:
                    Cost_per_provider_s += sum
                    sum_s += sum
                if data['Cost_per_provider'] % 100 == 35:
                    Cost_per_provider_u += sum
                    sum_u += sum

            if data['Cost_transfer_provider']:
                sum = (data['Cost_transfer_provider'] // 100)
                if data['Cost_transfer_provider'] % 100 == 33:
                    Cost_transfer_provider_d += sum
                    sum_d += sum
                if data['Cost_transfer_provider'] % 100 == 34:
                    Cost_transfer_provider_s += sum
                    sum_s += sum
                if data['Cost_transfer_provider'] % 100 == 35:
                    Cost_transfer_provider_u += sum
                    sum_u += sum

            if data['Cost_VIP_provider']:
                sum = (data['Cost_VIP_provider'] // 100)
                if data['Cost_VIP_provider'] % 100 == 33:
                    Cost_VIP_provider_d += sum
                    sum_d += sum
                if data['Cost_VIP_provider'] % 100 == 34:
                    Cost_VIP_provider_s += sum
                    sum_s += sum
                if data['Cost_VIP_provider'] % 100 == 35:
                    Cost_VIP_provider_u += sum
                    sum_u += sum

            sum_dict['Cost_extra_hour_provider_d'] = Cost_extra_hour_provider_d
            sum_dict['Cost_extra_hour_provider_s'] = Cost_extra_hour_provider_s
            sum_dict['Cost_extra_hour_provider_u'] = Cost_extra_hour_provider_u

            sum_dict['Cost_per_provider_d'] = Cost_per_provider_d
            sum_dict['Cost_per_provider_s'] = Cost_per_provider_s
            sum_dict['Cost_per_provider_u'] = Cost_per_provider_u

            sum_dict['Cost_transfer_provider_d'] = Cost_transfer_provider_d
            sum_dict['Cost_transfer_provider_s'] = Cost_transfer_provider_s
            sum_dict['Cost_transfer_provider_u'] = Cost_transfer_provider_u

            sum_dict['Cost_VIP_provider_d'] = Cost_VIP_provider_d
            sum_dict['Cost_VIP_provider_s'] = Cost_VIP_provider_s
            sum_dict['Cost_VIP_provider_u'] = Cost_VIP_provider_u

            sum_dict['sum_d'] = sum_d
            sum_dict['sum_s'] = sum_s
            sum_dict['sum_u'] = sum_u

            sum_dict['sum_d_m'] = sum_d*1.17
            sum_dict['sum_s_m'] = sum_s*1.17
            sum_dict['sum_u_m'] = sum_u*1.17
        print('sum dict: ', sum_dict)
        sum_table_fields = ['Cost_per_provider', 'Extra_hours_provider', 'Cost_transfer_provider', 'Cost_VIP_provider', 'sum', 'sum+maam']


    content = render_to_string('main/to_send.html', {'field_names': field_names, 'end_filter': end_filter,
                                                     'customer_bool': customer_bool,
                                                     'provider_bool': provider_bool,
                                                     'sum_dict': sum_dict,
                                                     'sum_table_fields': sum_table_fields}, request=request)
    print('mail to:', mail)
    msg = EmailMessage("caneti", content, to=[mail])
    # msg.attach('my_pdf.pdf', pdf, 'application/pdf')
    msg.content_subtype = "html"
    msg.send()

    # request.session['field_names'] = field_names
    # request.session['end_filter'] = end_filter
    return render(request, 'main/to_send.html', {'field_names': field_names, 'end_filter': end_filter})

    # print(project_num, customer, provider, min, max)
    # main_list_resource = main_list_Resource()
    # dataset = main_list_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    #
    # response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    #
    # return response

def to_send(request):
    print('to send view')
    field_names = request.session.get('field_names', '')

    # end_filter = request.session.get('end_filter', '')
    return render(request, 'main/to_send.html', {'field_names': field_names}) #, 'end_filter': model.query

def table_view(request):
    table = main_list_Table(main_list_model.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'main/table_view.html', {'table': table})


def intro(request):
    pass


def main_list(request):
    try:
        now = datetime.now()
        date = now.date()
        backup_date = request.session['back_up_date']
        print('try backup_date: ', datetime.strptime(backup_date, '%Y-%m-%d').date())
        delta = date - datetime.strptime(backup_date, '%Y-%m-%d').date()
        if delta.days > 1:
            print('1 days pased')
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
    table_all = main_list_Table(main_list_model.objects.all())
    RequestConfig(request).configure(table_upcoming)

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
                messages.success(request, ('Your order was successfully updated!'))
                return redirect('main_list')
            else:
                print('main list - got an error: ', form.errors)
                messages.error(request, ('Please correct the error below \n {}'.format(request.POST['From'])))

    else:
        form = main_list_form
        date_form = DateForm

    return render(request, 'main/main_list_model_form.html', {'form': form,
                                                              'field_names': field_names[1:],
                                                              'table_upcoming': table_upcoming,
                                                              'p_num_list': p_num_set,
                                                              'customer_list': customer_set,
                                                              'provider_list': provider_set,
                                                              'date_form': date_form})

def whole_list(request):

    table_all = main_list_Table(main_list_model.objects.all())
    RequestConfig(request).configure(table_all)

    # field_names = [f.name for f in main_list_model._meta.get_fields()]
    # all = main_list_model.objects.all().order_by('Date')
    # print('all: ', all)
    return render(request, 'main/whole_list.html', {'table_all': table_all})


def search_list(request):
    if request.method == 'POST':
        print('transfer -post')
        form = main_list_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your order was successfully updated!')
            return redirect('add_main_list')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = main_list_form
        field_names = [f.name for f in main_list_model._meta.get_fields()]
        # print(field_names)

        now = timezone.now()
        upcoming = main_list_model.objects.filter(Date__gte=now).order_by('Date')
        # passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        print(upcoming)
    return render(request, 'main/main_list_model_form.html', {'form': form, 'field_names': field_names[1:],
                                                              'upcoming': upcoming})

def p_num_list(request):
    p_num = request.GET.get('p_num_list')
    project_group = main_list_model.objects.filter(Project_num=p_num)
    field_names = [f.name for f in main_list_model._meta.get_fields()]
    # context = {'p_num': p_num}
    return render(request, 'main/project_group.html', {'field_names': field_names[1:], 'project_group': project_group})

def customer_list(request):
    customer = request.GET.get('customer_list')
    customer_group = main_list_model.objects.filter(Customer=customer)
    print('customer_list', customer_group)
    field_names = [f.name for f in main_list_model._meta.get_fields()]
    # context = {'p_num': p_num}
    return render(request, 'main/customer_group.html', {'field_names': field_names[1:],
                                                        'customer_group': customer_group})

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

def add_color(request):
    color = request.GET.get('color')
    if color == '':
        pass
    else:
        id = request.GET.get('id')
        td_id = request.GET.get('td_id')
        text_color = request.GET.get('text_color')
        print('text_color: ', text_color)

        old_color = main_list_model.objects.filter(pk=id)
        old_color_data = old_color.values()[0]['Color']
        if old_color_data == None:
            old_color_data = ''
        print('old_color: ', old_color_data)

        if text_color == 'true':
            main_list_model.objects.filter(pk=id).update(Color=old_color_data + td_id + '-' + color + '-' + text_color + '^')
            print('new text color: ', td_id + '-' + color + '-' + text_color + '^')
        else:
            main_list_model.objects.filter(pk=id).update(Color=old_color_data + td_id + '-' + color + '^')
            print('new color: ', td_id + '-' + color + '-' + '^')

    return JsonResponse({'is_taken': 'is_taken'})

class update(UpdateView):
    model = main_list_model
    form_class = main_list_form_update
    # fields = '__all__'
    success_url = reverse_lazy('main_list')
    template_name_suffix = '_update_form'

    # def convert_currnecy_sign(self, signed_num):
    #     if signed_num.startswith('$'):
    #         print('returning: ', signed_num.replace("$", "")+'33')
    #         return signed_num.replace("$", "")+'33'
    #
    # def get_form_kwargs(self):
    #     kwargs = super(update, self).get_form_kwargs()
    #     print('kwargs: ', kwargs)
    #     if 'data' in kwargs.keys():
    #         for key in kwargs['data'].keys():
    #             print('key: ', key)
    #             if kwargs['data'][key].startswith('$'):
    #                 print(kwargs['data'][key])
    #                 kwargs['instance'].key = self.convert_currnecy_sign(kwargs['data'][key])
    #     return kwargs

    def check_for_null(self, field, model, query_dicy=None):
        if field:
            return model.objects.get(**query_dicy).pk
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
        to_data = self.check_for_null(to_data_field, To_data, {'To': to_data_field})

        from_data_field = self.get_object().From
        from_data = self.check_for_null(from_data_field, From_data, {'From': from_data_field})

        car_data_field = self.get_object().Type_of_car
        car_data = self.check_for_null(car_data_field, Car_data, {'Car': car_data_field})

        flight_data_field = self.get_object().Flight_num
        flight_data = self.check_for_null(flight_data_field, Flight_data, {'Flight': flight_data_field})
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
'''
class add_to_main_list(CreateView):
    model = main_list_model
    fields = '__all__'
    success_url = reverse_lazy('add_to_main_list')

    def get_queryset(self):
        now = timezone.now()
        upcoming = main_list_model.objects.filter(Date__gte=now).order_by('Date')
        # passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        print(upcoming)
        try:
            return upcoming
        except TypeError as e:
            self.context_object_name = 'error'
            return ['there is an error', e]

class main_list(ListView):
    template_name = 'main/main_list.html'
    model = main_list_model
    # https://stackoverflow.com/questions/5358800/django-listing-model-field-names-and-values-in-template

    def get_queryset(self):
        now = timezone.now()
        # upcoming = transfer.objects.filter(Date__gte=now).order_by('Date')
        passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        # print(passed)
        try:
            trans_proj_list = get_transfer_and_project()
            return trans_proj_list
        except TypeError as e:
            self.context_object_name = 'error'
            return ['there is an error', e]



def get_transfer_and_project():
    # https://howchoo.com/g/yzzkodmzzmj/combine-two-querysets-with-different-models
    # https://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view
    transfers = transfer.objects.filter()
    projects = Proj.objects.filter()

    trans_and_proj = sorted(chain(transfers, projects), key=lambda row: row.Date, reverse=True)

    return trans_and_proj

class ProjCreate(CreateView):
    model = Proj
    fields = '__all__'
    success_url = reverse_lazy('project_detail_add')

class ProjUpdate(UpdateView):
    model = Proj
    fields = '__all__'

class ProjDelete(DeleteView):
    model = Proj
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('transfer_list')

class project_detailCreate(CreateView):
    template_name = 'main/project_form.html'
    # model = project
    form_class = project_form
    # fields = '__all__'
    success_url = reverse_lazy('Proj_list')
    # got an error when used this reverse circuler import ?
    # https://stackoverflow.com/questions/30460461/django-reverse-causes-circular-import/30460531

class project_detailUpdate(UpdateView):
    model = project
    fields = '__all__'
    success_url = reverse_lazy('transfer_list')
    # got an error when used this reverse circuler import ?

class project_detailDelete(DeleteView):
    model = project
    success_url = reverse_lazy('transfer_list')


class ProjListView(ListView):
    template_name = 'main/Proj_list.html'
    model = Proj


class TransferListView(ListView):
    template_name = 'main/transfer_list.html'
    model = transfer
    # https://stackoverflow.com/questions/5358800/django-listing-model-field-names-and-values-in-template

    def get_queryset(self):
        now = timezone.now()
        # upcoming = transfer.objects.filter(Date__gte=now).order_by('Date')
        passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        # print(passed)
        try:
            trans_proj_list = get_transfer_and_project()
            return trans_proj_list
        except TypeError as e:
            self.context_object_name = 'error'
            return ['there is an error', e]




    # def get_context_data(self, **kwargs):
    #     context = super(TransferListView, self).get_context_data(**kwargs)
    #     context.update({
    #         'project_list': project.objects.order_by('Date'),
    #
    #     })
    #     return context

class ProjectListView(ListView):
    # print('project list view')
    template_name = 'main/project_list.html'
    model = project
    # https://stackoverflow.com/questions/5358800/django-listing-model-field-names-and-values-in-template

    def get_queryset(self):
        now = timezone.now()
        pk = self.kwargs['pk']
        print('project pk: ', pk)
        # https://stackoverflow.com/questions/8164675/chaining-multiple-filter-in-django-is-this-a-bug
        # upcoming = transfer.objects.filter(Date__lte=now).order_by('Date')
        passed = project.objects.filter(Date__gte=now, Proj_ref=pk).order_by('Date')
        return list(passed)

def homepage(request):
    if request.method == 'POST':
        print('transfer -post')
        form = transfer_form(request.POST)

        if form.is_valid():
            for key, value in form.cleaned_data.items():
                print('key: ', key, 'val: ', value)

            form.save()

            # proj = False
            # for key, value in form.cleaned_data.items():
            #     if key == 'Project' and value == 'yes':
            #         proj = True
            # if proj:
            #     # messages.success(request, ('A Project was detected'))
            #     return redirect('project')
            # else:
            #     messages.success(request, ('Your order was successfully updated!'))
            #     return redirect('thankyou')
            messages.success(request, ('Your order was successfully updated!'))
            return redirect('homepage')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = transfer_form
    return render(request, 'main/index.html', {'form': form})


# def project_view(request):
#     if request.method == 'POST':
#         form = project_form(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('homepage')
#         else:
#             messages.error(request,('Please correct the error below.'))
#     else:
#         form = project_form
#     return render(request, 'main/project.html', {'form': form})

class transfer_update(UpdateView):
    model = transfer
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('transfer_list')

class transfer_delete(DeleteView):
    model = transfer
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('transfer_list')
'''