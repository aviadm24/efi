from django.contrib import admin
from .models import Service_data, Flight_data, Car_data, Provider_data\
                    , Driver_data, Customer_data, main_list_model, Status_data\
                    , From_data, To_data, Yeruka_data, Yeruka2_data, Fields_to_cancel
from import_export import resources


class main_list_modelAdmin(admin.ModelAdmin):

    list_display = ('id', 'Project_num', 'Date')
    search_fields = ('Project_num', 'Date')

admin.site.register(Service_data)
admin.site.register(Status_data)
admin.site.register(Car_data)
admin.site.register(Flight_data)
admin.site.register(Provider_data)
admin.site.register(Driver_data)
admin.site.register(Customer_data)
admin.site.register(main_list_model, main_list_modelAdmin)
admin.site.register(Fields_to_cancel)
admin.site.register(From_data)
admin.site.register(To_data)
admin.site.register(Yeruka_data)
admin.site.register(Yeruka2_data)


class main_list_Resource(resources.ModelResource):

    class Meta:
        model = main_list_model