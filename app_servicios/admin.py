from django.contrib import admin
from app_servicios.models import servicio

# Register your model here

class servicioadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   



admin.site.register(servicio, servicioadmin)