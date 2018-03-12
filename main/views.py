from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import transfer_form, project_form, form_data_Customer_ref
from django.forms import formset_factory
from django.views.generic.list import ListView
from django.utils import timezone
from .models import transfer, project

# http://jsfiddle.net/QLfMU/116/
class TransferListView(ListView):
    template_name = 'main/transfer_list.html'
    model = transfer
    # https://stackoverflow.com/questions/5358800/django-listing-model-field-names-and-values-in-template
    def get_queryset(self):
        now = timezone.now()
        # upcoming = transfer.objects.filter(Date__gte=now).order_by('Date')
        passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        print(passed)
        return list(passed) #+ list(passed)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

class ProjectListView(ListView):
    template_name = 'main/project_list.html'
    model = project
    # https://stackoverflow.com/questions/5358800/django-listing-model-field-names-and-values-in-template
    def get_queryset(self):
        now = timezone.now()
        # upcoming = transfer.objects.filter(Date__gte=now).order_by('Date')
        passed = transfer.objects.filter(Date__lt=now).order_by('Date')
        print(passed)
        return list(passed) #+ list(passed)

def customer_view(request):
    customer_FormSet = formset_factory(form_data_Customer_ref, extra=2)
    if request.method == 'POST':
        formset = customer_FormSet(request.POST)
        if formset.is_valid():
        #forms = formset.save(commit=False)
            for form in formset:
                print('form: ',form.as_table())
                form = form.save(commit=False)
                # form.user = request.user
                # print(form.user)
                form.save()
        return redirect('homepage')
    else:
        formset = customer_FormSet()
        return render(request, 'main/customer_data.html', {'formset': formset})

def homepage(request):
    if request.method == 'POST':
        form = transfer_form(request.POST)
        if form.is_valid():
            form.save()
            for key, value in form.cleaned_data.items():
                if key == 'Project' and value == 'yes':
                    proj = True
            if proj:
                messages.success(request, ('A Project was detected'))
                return redirect('project')
            else:
                messages.success(request, ('Your order was successfully updated!'))
                return redirect('thankyou')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = transfer_form
    return render(request, 'main/index.html', {'form': form})


def project(request):
    if request.method == 'POST':
        form = project_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('homepage')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = project_form
    return render(request, 'main/project.html', {'form': form})

