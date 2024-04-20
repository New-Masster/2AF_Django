from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Funcionario
from .models import Dependente
from .models import Departamento

admin.site.register(Funcionario)
admin.site.register(Dependente)
admin.site.register(Departamento)

