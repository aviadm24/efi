import django_tables2 as tables
from .models import main_list_model

class main_list_Table(tables.Table):
    class Meta:
        model = main_list_model
        template_name = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table', 'id': 'mainlist'}