from django.contrib import admin
from .models import transfer, formData, project

admin.site.register(transfer)
admin.site.register(project)
admin.site.register(formData)