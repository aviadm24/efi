from django.db import models
from django.contrib.postgres.fields import JSONField

from django.urls import reverse
#https://stackoverflow.com/questions/15454008/how-to-reset-db-in-django-i-get-a-command-reset-not-found-error
# python manage.py reset_db
# heroku pg:reset
class main_list_model(models.Model):
    Project_num = models.IntegerField(blank=True, null=True, verbose_name='Project number')
    Customer = models.CharField(max_length=100, blank=True, null=True, verbose_name='Reference customer')
    Contact = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    Type_of_service = models.CharField(max_length=256, blank=True, null=True)
    Type_of_car = models.CharField(max_length=256, blank=True, null=True)
    Name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Name client')
    Luggage = models.CharField(max_length=10, blank=True, null=True, verbose_name='Number of PAX & Luggage')  # changed to char field

    Flight_num = models.CharField(max_length=100, blank=True, null=True)
    Start_time = models.DateTimeField(blank=True, null=True)
    End_time = models.DateTimeField(blank=True, null=True)
    From = models.CharField(max_length=100, blank=True, null=True)
    To = models.CharField(max_length=100, blank=True, null=True)

    Provider = models.CharField(max_length=100, blank=True, null=True)
    Driver_name = models.CharField(max_length=100, blank=True, null=True)
    status_cheshbonit_yeruka1 = models.CharField(max_length=100, blank=True, null=True,
                                                 verbose_name='Status חשבונית ירוקה')  # new
    Comments = models.TextField(blank=True)
    Status = models.CharField(max_length=100, blank=True, null=True)
    status_cheshbonit_yeruka2 = models.CharField(max_length=100, blank=True, null=True,
                                                 verbose_name='Status חשבונית ירוקה')  # new
    Extra_hours_client = models.IntegerField(null=True, blank=True)
    Based_on_client = models.IntegerField(blank=True, null=True)
    Extra_hours_provider = models.IntegerField(null=True, blank=True)
    Based_on_provider = models.IntegerField(blank=True, null=True)  # , default='09:00'

    KM = models.IntegerField(blank=True, null=True)
    Extra_KM_client = models.IntegerField(blank=True, null=True)
    Extra_KM_provider = models.IntegerField(blank=True, null=True)
    Cost_per_client = models.IntegerField(blank=True, null=True)
    Cost_per_provider = models.IntegerField(blank=True, null=True)
    Cost_transfer_client = models.IntegerField(blank=True, null=True)
    Cost_transfer_provider = models.IntegerField(blank=True, null=True)
    Cost_extra_hour_client = models.IntegerField(blank=True, null=True)
    Cost_extra_hour_provider = models.IntegerField(blank=True, null=True)
    Cost_VIP_client = models.IntegerField(blank=True, null=True)
    Cost_VIP_provider = models.IntegerField(blank=True, null=True)

    Color = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return str(self.Project_num)

# class transfer(models.Model):
#
#     type_choice = (
#         ('Dep', 'Dep'),
#         ('Arr', 'Arr'),
#     )
#
#     Customer = models.CharField(max_length=100, blank=True, null=True)  # new
#     Customer_ref = models.CharField(max_length=100, blank=True, null=True)
#     Date = models.DateField(blank=True, null=True)
#     Driver = models.CharField(max_length=100, blank=True, null=True)
#     Provider = models.CharField(max_length=100, blank=True, null=True)
#     Car = models.CharField(max_length=100, blank=True, null=True)
#     Clients_Name = models.CharField(max_length=100, blank=True, null=True)
#     From = models.CharField(max_length=100, blank=True, null=True)  # new
#     To = models.CharField(max_length=100, blank=True, null=True)  # new
#     DepOrArr = models.NullBooleanField(blank=True, null=True, choices=type_choice)  # new models.NullBooleanField()
#     Flight = models.CharField(max_length=100, blank=True, null=True)
#     Time_of_flight = models.CharField(max_length=100, blank=True, null=True)  # new
#     Time_of_PU = models.CharField(max_length=100, blank=True, null=True)  # new
#     Contact = models.CharField(max_length=100, blank=True, null=True)
#     Project = models.CharField(max_length=100, blank=True, null=True)
#
#     def __str__(self):
#         return self.Customer_ref

    # def get_absolute_url(self):
    #     return reverse('transfer_update', args=(self.pk,))


class Flight_data(models.Model):  # new
    Flight = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Flight


class Customer_data(models.Model):  # new
    Customer_name = models.CharField(max_length=256, blank=True, unique=True)
    email = models.EmailField(max_length=250, blank=True, unique=False)
    phone_num = models.CharField(max_length=80, blank=True, unique=False)
    address = models.CharField(max_length=256, blank=True, unique=False)
    city = models.CharField(max_length=50, blank=True, unique=False)
    contact = models.CharField(max_length=50, blank=True, unique=False)
    id_num = models.CharField(max_length=30, blank=True, unique=False)
    used_a_lot = models.BooleanField(default=False)

    def __str__(self):
        return self.Customer_name


class Driver_data(models.Model):
    Driver = models.CharField(max_length=256, blank=True, unique=True)
    email = models.EmailField(max_length=250, blank=True, unique=False)
    phone_num = models.CharField(max_length=80, blank=True, unique=False)
    address = models.CharField(max_length=256, blank=True, unique=False)
    contact = models.CharField(max_length=50, blank=True, unique=False)
    id_num = models.CharField(max_length=30, blank=True, unique=False)

    def __str__(self):
        return self.Driver


class Provider_data(models.Model):
    Provider_name = models.CharField(max_length=256, blank=True, unique=True)
    email = models.EmailField(max_length=250, blank=True, unique=False)
    phone_num = models.CharField(max_length=80, blank=True, unique=False)
    address = models.CharField(max_length=256, blank=True, unique=False)
    city = models.CharField(max_length=100, blank=True, unique=False)
    contact = models.CharField(max_length=100, blank=True, unique=False)
    id_num = models.CharField(max_length=30, blank=True, unique=False)
    used_a_lot = models.BooleanField(default=False)

    def __str__(self):
        return self.Provider_name


class Car_data(models.Model):
    Car = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Car


class Service_data(models.Model):
    Service = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Service

class Status_data(models.Model):
    Status = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Status


class Yeruka_data(models.Model):
    Yeruka = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Yeruka


class Yeruka2_data(models.Model):
    Yeruka2 = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Yeruka2


class To_data(models.Model):
    To = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.To


class From_data(models.Model):
    From = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.From

                # class Proj(models.Model):
#     Proj_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
#     Date = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return self.Proj_name
#
#     def get_absolute_url(self):
#         return reverse('Proj_detail', kwargs={'pk': self.pk})
#
# class project(models.Model):
#     Proj_ref = models.ForeignKey(Proj, related_name='Proj_parts', on_delete=models.CASCADE)
#     Date = models.DateField(blank=True, null=True)
#     Name = models.CharField(max_length=256, blank=True, null=True)
#     Type_of_car = models.CharField(max_length=256, blank=True, null=True)
#     Type_of_service = models.CharField(max_length=256, blank=True, null=True)
#     Driver = models.CharField(max_length=256, blank=True, null=True)
#     Provider = models.CharField(max_length=256, blank=True, null=True)
#     Flight = models.CharField(max_length=256, blank=True, null=True)
#     Based_on = models.TimeField(max_length=256, blank=True, null=True, default='09:00')
#     Start_time = models.TimeField(blank=True, null=True)
#     End_time = models.TimeField(blank=True, null=True)
#     Extra_hours = models.TimeField(blank=True, null=True)
#     KM = models.IntegerField(blank=True, null=True)
#     Extra_KM = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.pk)