from django import forms



sexo=(
('Masculino',"M"),
('Femenino', "F"),
)

Tipo_Sangre = (
('O+', 'O+',),
('O-', 'O-'),
('A+', 'A+'),
('A-', 'A-'),
('B+', 'B+'),
('B-', 'B-'),
('AB+', 'AB+'),
('AB-', 'AB-'),
)
class RegConsulta(forms.Form):
    fecha_consulta = forms.CharField()
    doctor = forms.CharField(max_length=100)
    paciente = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=sexo)
    motivo_consulta = forms.CharField()
    diagnostico = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Enfermedad o estado del paciente'}))

    indicaciones_medicas = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Tratamientos que tiene que seguir el paciente.'}))

class RegPersonal(forms.Form):
        nombre = forms.CharField(max_length = 30)
        edad = forms.DecimalField(max_digits=100, decimal_places=2)
        fechaNacimiento = forms.CharField()
        Tipo_Sangre = forms.ChoiceField(choices=Tipo_Sangre)
        patologias = forms.CharField(max_length=100)
        email = forms.EmailField()
