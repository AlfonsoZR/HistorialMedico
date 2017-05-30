# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
from .forms import RegConsulta, RegPacientes, RegAlergias
from .models import Pacientes, Alergias_Medicamentos, Consultas

from django.db.models import Q
from mimetypes import guess_type
from wsgiref.util import FileWrapper
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
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
    form = RegPacientes(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        dato = form_data.get("nombre")
        dato2 = form_data.get("edad")
        dato3 = form_data.get("fechaNacimiento")
        dato4 = form_data.get("Tipo_Sangre")
        dato5 = form_data.get("Alergias")
        dato6 = form_data.get("email")

        obj = Pacientes.objects.create(nombre=dato, edad=dato2,fechaNacimiento=dato3,
        Tipo_Sangre=dato4,Alergias=dato5, email=dato6)
    context ={
    "Info_Personal": form,
    }

    return render(request,"InfPersonal.html", context)



#vista para crear una visita
def Crear_consulta (request):
    form = RegConsulta(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        c = form_data.get("paciente")
        c2 = form_data.get("motivo")
        c3 = form_data.get("problema")
        c4 = form_data.get("NotaMedic")

        obj = Consultas.objects.create(paciente=c, motivo=c2, problema=c3, NotaMedic=c4)
    context ={
    "crear_visita": form,
    }

    return render(request,"VisitaCrear.html", context)
#vista para mirar las visitas que tenemos acumuladas
class VisitasListView(ListView):
    model = Consultas

    def get_queryset(self, *args, **kwargs):
        qs = super(VisitasListView, self).get_queryset(**kwargs)

        busca = self.request.GET.get("q")
        if busca:
            qset = (
                Q(paciente__icontains=busca)

            )
            qs = Consultas.objects.filter(qset).distinct()

        return qs



#vista basada en clases para aver datos personales.
class DatosUserListView(ListView):
    model = Pacientes

    def get_queryset(self, *args, **kwargs):
        qs = super(DatosUserListView, self).get_queryset(**kwargs)

        busca = self.request.GET.get("q")
        if busca:
            qset = (
                Q(nombre__icontains=busca)

            )
            qs = Pacientes.objects.filter(qset).distinct()

        return qs

#alergias crear
def Crear_alergia (request):
    form = RegAlergias(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        d = form_data.get("medicamento")
        d2 = form_data.get("motivo")
        d3 = form_data.get("alergias")

        obj = Alergias_Medicamentos.objects.create(medicamento=d, motivo=d2,alergias=d3,)
    context ={
    "crear_alergia": form,
    }

    return render(request,"AlergiasCrear.html", context)
#alergias vistas
class AlergiasListView(ListView):
    model = Alergias_Medicamentos

    def get_queryset(self, *args, **kwargs):
        qs = super(AlergiasListView, self).get_queryset(**kwargs)

        # busca = self.request.GET.get("q")
        # if busca:
        #     qset = (
        #         Q(nombre__icontains=busca) |
        #         Q(autor__icontains=busca)
        #     )
        #     qs = Libro.objects.filter(qset).distinct()

        return qs


def useropc (request):
    return render(request, "usuarioopc.html")

class PacientesUpdateView(UpdateView):
    model = Pacientes
#    template_name = "form.html"
    fields=["nombre","email", "Alergias" ]
    template = "InfPersonal.html"
    success_url = "/DatosUser/lista"

# class DatosAlergias(CreateView):
#     model = Alergias_Medicamentos
# #   template_name = "form.html"
#     form_class = RegAlergias
#     #success_url = "/producto/crear/"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(DatosAlergias, self).get_context_data(*args, **kwargs)
#         context["submit_btn"]="Guardar"
#         return context
#
# class DatosVisitas(CreateView):
#     model = Visitas
# #   template_name = "form.html"
#     form_class = Regvisitas
#     #success_url = "/producto/crear/"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(DatosVisitas, self).get_context_data(*args, **kwargs)
#         context["submit_btn"]="Guardar"
#         return context
