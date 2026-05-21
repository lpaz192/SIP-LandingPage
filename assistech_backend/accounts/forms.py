from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='Nombre')
    last_name  = forms.CharField(max_length=50, label='Apellido')
    email      = forms.EmailField(required=True)
    
    TIPOS_USUARIO = [
        ('CLIENTE', 'Cliente / Usuario Normal'),
        ('SOPORTE', 'Soporte Técnico'),
        ('JEFE', 'Jefe de Soporte'),
    ]
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIO, label='Tipo de Cuenta')
    
    empresa = forms.CharField(max_length=100, label='Empresa', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'tipo_usuario', 'empresa']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ese nombre de usuario ya está en uso.')
        return username

class LoginForm(forms.Form):
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')