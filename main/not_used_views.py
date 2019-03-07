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
