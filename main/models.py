from django.db import models
# from django.contrib.postgres.fields import JSONField
# https://github.com/psycopg/psycopg2/issues/329

from django.urls import reverse
#https://stackoverflow.com/questions/15454008/how-to-reset-db-in-django-i-get-a-command-reset-not-found-error
# python manage.py reset_db
# heroku pg:reset

# backups
# Asia/Jerusalem
class main_list_model(models.Model):
    Project_num = models.CharField(max_length=100, blank=True, null=True, verbose_name='Project number')
    Customer_num = models.CharField(max_length=100, blank=True, null=True, verbose_name='Client Reference Number')
    Customer = models.CharField(max_length=100, blank=True, null=True, verbose_name='Reference customer')
    Contact = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    Type_of_service = models.CharField(max_length=256, blank=True, null=True)
    Type_of_car = models.CharField(max_length=256, blank=True, null=True)
    Name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Name client')
    Luggage = models.CharField(max_length=10, blank=True, null=True, verbose_name='Number of PAX & Luggage')  # changed to char field

    Flight_num = models.CharField(max_length=100, blank=True, null=True)
    # changing from time field to date time field made a big problem
    # https: // stackoverflow.com / questions / 15237366 / how - to - execute - a - sql - script - on - heroku
    # https: // stackoverflow.com / questions / 23892307 / django - change - timefield - to - datetimefield - in -models - py / 39104671
    # https: // stackoverflow.com / questions / 10200769 / postgresql - column - foo - does - not -exist
    # https: // www.postgresql.org / docs / 9.1 / datatype - datetime.html
    # very importent to know!
    Flight_shcedule = models.DateTimeField(blank=True, null=True)
    Start_time = models.DateTimeField(blank=True, null=True)
    End_time = models.DateTimeField(blank=True, null=True)
    From = models.CharField(max_length=100, blank=True, null=True)
    To = models.CharField(max_length=100, blank=True, null=True)

    Provider = models.CharField(max_length=100, blank=True, null=True)
    Driver_name = models.CharField(max_length=100, blank=True, null=True)
    Provider_status = models.CharField(max_length=100, blank=True, null=True,
                                       verbose_name='Status Provider')  # new
    Comments = models.TextField(blank=True)
    Status = models.CharField(max_length=100, blank=True, null=True, verbose_name='Project Status')
    Client_status = models.CharField(max_length=100, blank=True, null=True,
                                     verbose_name='Status Client')  # new
    Extra_hours_client = models.FloatField(null=True, blank=True)
    Based_on_client = models.FloatField(blank=True, null=True)
    Extra_hours_provider = models.FloatField(null=True, blank=True)
    Based_on_provider = models.FloatField(blank=True, null=True)  # , default='09:00'

    KM = models.IntegerField(blank=True, null=True)
    Extra_KM_client = models.IntegerField(blank=True, null=True)
    Extra_KM_provider = models.IntegerField(blank=True, null=True)
    Cost_per_client = models.CharField(max_length=100, blank=True, null=True)
    Cost_per_provider = models.CharField(max_length=100, blank=True, null=True)
    Cost_transfer_client = models.CharField(max_length=100, blank=True, null=True)
    Cost_transfer_provider = models.CharField(max_length=100, blank=True, null=True)
    Cost_extra_hour_client = models.CharField(max_length=100, blank=True, null=True)
    Cost_extra_hour_provider = models.CharField(max_length=100, blank=True, null=True)
    Cost_VIP_client = models.CharField(max_length=100, blank=True, null=True)
    Cost_VIP_provider = models.CharField(max_length=100, blank=True, null=True)

    Cost_shonot_client = models.CharField(max_length=100, blank=True, null=True)
    Cost_shonot_provider = models.CharField(max_length=100, blank=True, null=True)

    Color = models.CharField(max_length=3000, blank=True, null=True)
    Canceled = models.NullBooleanField(blank=True, null=True)
    # Canceled = models.BooleanField(default=False)

    def update_field(self, key, value):
        # This will raise an AttributeError if the key isn't an attribute
        # of your model
        # https://stackoverflow.com/questions/21797436/django-how-to-update-model-field-from-json-data
        getattr(self, key)
        setattr(self, key, value)

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


class Fields_to_cancel(models.Model):
    Currency_field = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Currency_field
