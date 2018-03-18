from django.db import models
from django.urls import reverse
#https://stackoverflow.com/questions/15454008/how-to-reset-db-in-django-i-get-a-command-reset-not-found-error
# python manage.py reset_db
class transfer(models.Model):
    # user = models.ForeignKey(User, related_name='user_ishi', on_delete=models.CASCADE)
    Customer_ref = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    Driver = models.CharField(max_length=100, blank=True, null=True)
    Provider = models.CharField(max_length=100, blank=True, null=True)
    Car = models.CharField(max_length=100, blank=True, null=True)
    Clients_Name = models.CharField(max_length=100, blank=True, null=True)
    Service_from_to = models.CharField(max_length=100, blank=True, null=True)
    Flight = models.CharField(max_length=100, blank=True, null=True)
    Time_from_to = models.CharField(max_length=100, blank=True, null=True)
    Contact = models.CharField(max_length=100, blank=True, null=True)
    Project = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Customer_ref

    # def get_absolute_url(self):
    #     return reverse('transfer_update', args=(self.pk,))

class Customer_ref_data(models.Model):
    Customer_ref = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Customer_ref


class Driver_data(models.Model):
    Driver = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Driver


class Provider_data(models.Model):
    Provider = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Provider


class Car_data(models.Model):
    Car = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Car


class Model_data(models.Model):
    Model = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.Model

class Proj(models.Model):
    Proj_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Proj_name

    def get_absolute_url(self):
        return reverse('Proj_detail', kwargs={'pk': self.pk})

class project(models.Model):
    Proj_ref = models.ForeignKey(Proj, related_name='Proj_parts', on_delete=models.CASCADE)
    Date = models.DateField(blank=True, null=True)
    Name = models.CharField(max_length=256, blank=True, null=True)
    Type_of_car = models.CharField(max_length=256, blank=True, null=True)
    Type_of_service = models.CharField(max_length=256, blank=True, null=True)
    Driver = models.CharField(max_length=256, blank=True, null=True)
    Provider = models.CharField(max_length=256, blank=True, null=True)
    Flight = models.CharField(max_length=256, blank=True, null=True)
    Based_on = models.TimeField(max_length=256, blank=True, null=True, default='09:00')
    Start_time = models.TimeField(blank=True, null=True)
    End_time = models.TimeField(blank=True, null=True)
    Extra_hours = models.TimeField(blank=True, null=True)
    KM = models.IntegerField(blank=True, null=True)
    Extra_KM = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)