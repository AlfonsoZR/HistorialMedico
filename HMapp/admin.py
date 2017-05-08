# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import DatosUser

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    list_display=["nombre","email","edad","fechaNacimiento","Tipo_Sangre","patologias"]
    search_fields = ["nombre","email"]
    list_editable = ["email","patologias"]
    list_filter = ["fechaNacimiento","edad"]
    class Meta:
        model = DatosUser


admin.site.register(DatosUser, AdminUsuario)
