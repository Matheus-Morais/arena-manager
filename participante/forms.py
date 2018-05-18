from django import forms
from .models import *

class ParticipanteForms(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'