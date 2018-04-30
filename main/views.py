from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import main_list_form
from django.forms import formset_factory
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .models import  main_list_model
from itertools import chain

# https://stackoverflow.com/questions/20926403/heroku-rake-dbmigrate-results-in-error-r13-attach-error-failed-to-attach-t/21148716#21148716
# http://jsfiddle.net/QLfMU/116/

def add_main_list(request):
    field_names = [f.name for f in main_list_model._meta.get_fields()]
    now = timezone.now()
    #  https://stackoverflow.com/questions/7503241/django-models-selecting-single-field
    # p_num_list = main_list_model.objects.values_list('Project_num', flat=True)
    p_num_filterd_list = main_list_model.objects.filter(Date__gte=now).values_list('Project_num', flat=True)
    for i in p_num_filterd_list:
        print('p_num_filterd_list:', i)
    customer_filterd_list = main_list_model.objects.filter(Date__gte=now).values_list('Customer', flat=True)

    upcoming = main_list_model.objects.filter(Date__gte=now).order_by('Date')
    all = main_list_model.objects.all()
    # passed = transfer.objects.filter(Date__lt=now).order_by('Date')
    print('all: ', all)
    print('upcoming: ', upcoming)

    if request.method == 'POST':
        print('main list - post')
        form = main_list_form(request.POST)
        if form.is_valid():
            # for key, value in form.cleaned_data.items():
            #     if key == 'Date':
            #         print('key: ', key, 'val: ', value)
            form.save()
            messages.success(request, ('Your order was successfully updated!'))
            return redirect('add_main_list')
        else:
            print('main list - got an error: ', form.errors)
            messages.error(request, ('Please correct the error below.'))
    else:
        form = main_list_form

    return render(request, 'main/main_list_model_form.html', {'form': form, 'field_names': field_names[1:], 'upcoming': upcoming, 'p_num_list': p_num_filterd_list, 'customer_list': customer_filterd_list})

def search_list(request):
    if request.method == 'POST':
        print('transfer -post')
        form = main_list_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your order was successfully updated!'))
            return redirect('add_main_list')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = main_list_form
        field_names = [f.name for f in main_list_model._meta.get_fields()]
        # print(field_names)

        now = timezone.now()
        upcoming = main_list_model.objects.filter(Date__gte=now).order_by('Date')
        # passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        print(upcoming)
    return render(request, 'main/main_list_model_form.html', {'form': form, 'field_names': field_names[1:],'upcoming': upcoming})

def p_num_list(request):
    p_num = request.GET.get('p_num_list')
    project_group = main_list_model.objects.filter(Project_num=p_num)
    field_names = [f.name for f in main_list_model._meta.get_fields()]
    # context = {'p_num': p_num}
    return render(request, 'main/project_group.html', {'field_names': field_names[1:], 'project_group': project_group})

def customer_list(request):
    customer = request.GET.get('customer_list')
    customer_group = main_list_model.objects.filter(Customer=customer)
    field_names = [f.name for f in main_list_model._meta.get_fields()]
    # context = {'p_num': p_num}
    return render(request, 'main/customer_group.html', {'field_names': field_names[1:], 'customer_group': customer_group})

class update_row(UpdateView):
    model = main_list_model
    fields = '__all__'
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