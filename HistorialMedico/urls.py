"""HistorialMedico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from HMapp import views
from django.conf.urls import url, include
from contacto.views import UserRegisterView
from HMapp.views import DatosUserListView, VisitasListView, AlergiasListView, PacientesUpdateView
urlpatterns = [


url(r'^usuario', views.useropc, name='usuarioopc'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', UserRegisterView.as_view(), name='Registro'),

    url(r'^admin/', admin.site.urls),

    url(r'^crear/visita/', views.Crear_consulta, name='VisitasCrear'),

    url(r'^$', views.home, name='home'),

    url(r'^inicio/$', views.inicio, name='inicio'),

    url(r'^InfoPersonal/', views.InfPersonal, name='InfPersonal'),

    url(r'^DatosUser/lista$', DatosUserListView.as_view(), name='DatosUser_list'),

    url(r'^Visitas/lista$', VisitasListView.as_view(), name='Visitas_list'),

    url(r'^crear/alergia/', views.Crear_alergia, name='AlergiasCrear'),

    # url(r'^Alergias/lista$', AlergiasListView.as_view(), name='Alergias_list'),

    url(r'^paciente_actualizar/(?P<pk>\d+)/$', PacientesUpdateView.as_view(), name='update_paciente'),





    # url(r'^crear$', DatosAlergias.as_view(), name='DatosUser_crear'),
    #
    # url(r'^visitas$', DatosVisitas.as_view(), name='DatosVisitas_crear'),

]
