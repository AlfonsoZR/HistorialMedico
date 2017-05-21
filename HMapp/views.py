# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegConsulta, RegPersonal
from .models import DatosUser

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

def home(request):
    #Logico de negocio alias hechizo
    m = "Mi Historial Medico. :)"
    contexto= {"mensaje":m}
    return render(request, 'home.html', contexto)


def inicio (request):
    form = RegConsulta(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("doctor")
        abc2 = form_data.get("paciente")
    context = {
    "formConsulta": form,
    }

    return render(request, "inicio.html", context)

def InfPersonal (request):
    form = RegPersonal(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        dato = form_data.get("nombre")
        dato2 = form_data.get("edad")
        dato3 = form_data.get("fechaNacimiento")
        dato4 = form_data.get("Tipo_Sangre")
        dato5 = form.data.get("patologias")
        dato6 = form_data.get("email")

        obj = DatosUser.objects.create(nombre=dato, edad=dato2,fechaNacimiento=dato3,
        Tipo_Sangre=dato4,patologias=dato5, email=dato6)
    context ={
    "Info_Personal": form,
    }

    return render(request,"InfPresonal.html", context)




class DatosUserListView(ListView):
    model = DatosUser

    def get_queryset(self, *args, **kwargs):
        qs = super(DatosUserListView, self).get_queryset(**kwargs)

        # busca = self.request.GET.get("q")
        # if busca:
        #     qset = (
        #         Q(nombre__icontains=busca) |
        #         Q(autor__icontains=busca)
        #     )
        #     qs = Libro.objects.filter(qset).distinct()

        return qs
