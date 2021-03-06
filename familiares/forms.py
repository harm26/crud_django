from django import forms
from django.forms import ModelForm
from .models import *

class FormFamiliares(forms.ModelForm):
    class Meta:
        model= Familiares
        fields= '__all__'

