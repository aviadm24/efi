from django.contrib import admin
from .models import Service_data ,Flight_data, Car_data, Provider_data\
                    , Driver_data, Customer_data, main_list_model

# admin.site.register(transfer)
# admin.site.register(Proj)
# admin.site.register(project)
admin.site.register(Service_data)
admin.site.register(Car_data)
admin.site.register(Flight_data)
admin.site.register(Provider_data)
admin.site.register(Driver_data)
admin.site.register(Customer_data)
admin.site.register(main_list_model)