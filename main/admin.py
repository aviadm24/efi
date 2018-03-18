from django.contrib import admin
from .models import transfer, project, Model_data, Car_data, Provider_data\
                    ,Driver_data, Customer_ref_data, Proj

admin.site.register(transfer)
admin.site.register(Proj)
admin.site.register(project)
admin.site.register(Model_data)
admin.site.register(Car_data)
admin.site.register(Provider_data)
admin.site.register(Driver_data)
admin.site.register(Customer_ref_data)