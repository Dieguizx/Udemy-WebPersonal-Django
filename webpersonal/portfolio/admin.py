from django.contrib import admin
from .models import Project     # importar haciendo referencia a la propia app 'portfolio'

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):       # para mostrar los campos 'fecha de creacion' y 'fecha de modificacion' en forma de solo lectura a traves de una tupla
    readonly_fields = ('created', 'updated')   


admin.site.register(Project, ProjectAdmin)      # registrar el modelo

