# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pacientes, Consultas, Alergias_Medicamentos

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    list_display=["nombre","email","edad","fechaNacimiento","Tipo_Sangre","Alergias"]
    search_fields = ["nombre","email","Alergias"]
    list_editable = ["email"]
    list_filter = ["fechaNacimiento","edad"]
    class Meta:
        model = Pacientes


admin.site.register(Pacientes, AdminUsuario)

class adminvisitas(admin.ModelAdmin):
    list_display=["paciente","motivo","problema","NotaMedic"]
    search_fields = ["doctor"]
    list_filter = ["problema","NotaMedic","motivo"]
    class Meta:
        model = Consultas

admin.site.register(Consultas, adminvisitas)

class adminalergias(admin.ModelAdmin):
    list_display=["medicamento","motivo","alergias"]
    search_fields = ["medicamento"]
    list_filter = ["alergias","motivo"]
    class Meta:
        model = Alergias_Medicamentos

admin.site.register(Alergias_Medicamentos, adminalergias)
