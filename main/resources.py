from import_export import resources
from .models import main_list_model

class main_list_Resource(resources.ModelResource):
    class Meta:
        model = main_list_model