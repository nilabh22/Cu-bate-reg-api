from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registration
from django import forms


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'rollNo': forms.TextInput(),
            'email': forms.TextInput(),
            'phone':forms.TextInput(),
            'branch': forms.TextInput()
        }