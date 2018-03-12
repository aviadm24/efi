from django.db import models

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
    KM = models.IntegerField(blank=True, null=True)
    Contact = models.CharField(max_length=100, blank=True, null=True)
    Project = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Customer_ref

class formData(models.Model):
    Customer_ref = models.CharField(max_length=256, blank=True)
    Driver = models.CharField(max_length=256, blank=True)
    Provider = models.CharField(max_length=256, blank=True)
    Car = models.CharField(max_length=256, blank=True)
    Model = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.Customer_ref

class project(models.Model):
    # received_by = models.ForeignKey(transfer)
    Date = models.DateField(blank=True, null=True)
    Name = models.CharField(max_length=256, blank=True, null=True)
    Type_of_car = models.CharField(max_length=256, blank=True, null=True)
    Type_of_service = models.CharField(max_length=256, blank=True, null=True)
    Driver = models.CharField(max_length=256, blank=True, null=True)
    Provider = models.CharField(max_length=256, blank=True, null=True)
    Flight = models.CharField(max_length=256, blank=True, null=True)
    Based_on = models.CharField(max_length=256, blank=True, null=True)
    Start_time = models.DateField(blank=True, null=True)
    End_time = models.DateField(blank=True, null=True)
    Extra_hours = models.IntegerField(blank=True, null=True)
    KM = models.IntegerField(blank=True, null=True)
    Extra_KM = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name