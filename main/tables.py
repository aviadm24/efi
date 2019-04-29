import django_tables2 as tables
from .models import main_list_model

class main_list_Table(tables.Table):
    class Meta:
        model = main_list_model
        template_name = 'django_tables2/table.html'
        attrs = {'class': 'table',
                 'id': 'mainlist',
                 'border': '1',
                 'td': {'style': "border: 1px solid black;"}
                 }

