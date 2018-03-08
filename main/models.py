from django.db import models

class transfer(models.Model):
    # user = models.ForeignKey(User, related_name='user_ishi', on_delete=models.CASCADE)
    Customer_ref = models.CharField(max_length = 100)
    Date = models.DateField(blank=True, null=True)
    Driver = models.CharField(max_length = 100)
    Provider = models.CharField(max_length = 100)
    Car = models.CharField(max_length = 100)
    Clients_Name = models.CharField(max_length = 100)
    Service_from_to = models.CharField(max_length = 100)
    Flight = models.CharField(max_length = 100)
    Time_from_to = models.CharField(max_length = 100)
    KM = models.CharField(max_length = 100)
    Contact = models.CharField(max_length = 100)
    Project = models.CharField(max_length = 100)

    def __str__(self):
        return self.Customer_ref

class formData(models.Model):
    Customer_ref = models.CharField(max_length=256)
    Driver = models.CharField(max_length=256)
    Provider = models.CharField(max_length=256)
    Car = models.CharField(max_length=256)
    Model = models.CharField(max_length=256)

    def __str__(self):
        return self.Customer_ref

class project(models.Model):
    # received_by = models.ForeignKey(transfer)
    received_by = models.CharField(max_length=256)
    client_first_name = models.CharField(max_length=256)
    client_last_name = models.CharField(max_length=256)
    notes = models.TextField()
    status = models.IntegerField(choices=[[1, 'Open'], [2, 'Close']])