from django import forms
from .models import *

class ParticipanteForms(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'

class PartidaForms(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

class PartidaFIFAForms(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartidaFIFAForms, self).__init__(*args, **kwargs)
        self.fields['participante_casa'].queryset = Participante.objects.filter(jogo = 'FIFA')
        self.fields['participante_desafiante'].queryset = Participante.objects.filter(jogo = 'FIFA')

class PartidaLOLForms(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartidaLOLForms, self).__init__(*args, **kwargs)
        self.fields['participante_casa'].queryset = Participante.objects.filter(jogo = 'LOL')
        self.fields['participante_desafiante'].queryset = Participante.objects.filter(jogo = 'LOL')

class PartidaCSGOForms(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartidaCSGOForms, self).__init__(*args, **kwargs)
        self.fields['participante_casa'].queryset = Participante.objects.filter(jogo = 'CSGO')
        self.fields['participante_desafiante'].queryset = Participante.objects.filter(jogo = 'CSGO')