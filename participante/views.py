from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def lista_participantes_lol(request):
    participantes = Participante.objects.filter(jogo = 'LOL')
    return render(request, 'participantes/lista_participantes.html', {'participantes': participantes})

@login_required
def lista_participantes_fifa(request):
    participantes = Participante.objects.filter(jogo = 'FIFA')
    return render(request, 'participantes/lista_participantes.html', {'participantes': participantes})

@login_required
def lista_participantes_cs(request):
    participantes = Participante.objects.filter(jogo = 'CSGO')
    return render(request, 'participantes/lista_participantes.html', {'participantes': participantes})

@login_required
def novo_participante(request):
    if request.method == 'POST':
        form = ParticipanteForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('participantes:novo-participante')
        else:
            print(form.errors)
    else:
        form = ParticipanteForms()

    return render(request, 'participantes/novo_participante.html', {'form': form})

@login_required
def editar_participante(request, id):
    participante = get_object_or_404(Participante, id=id)
    if request.method == 'POST':
        form = ParticipanteForms(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            if participante.jogo == 'LOL':
                return redirect('participantes:lista-participantes-LOL')
            elif participante.jogo == 'FIFA':
                return redirect('participantes:lista_participantes_FIFA')
            elif participante.jogo == 'CSGO':
                return redirect('participantes:lista_participantes_CSGO')
    else:
        form = ParticipanteForms(instance=participante)
        return render(request, 'participantes/novo_participante.html', {'form': form})

@login_required
def excluir_participante(request, id):
    participante = Participante.objects.get(pk=id)
    participante.delete()
    if participante.jogo == 'LOL':
        return redirect('participantes:lista-participantes-LOL')
    elif participante.jogo == 'FIFA':
        return redirect('participantes:lista_participantes_FIFA')
    elif participante.jogo == 'CSGO':
        return redirect('participantes:lista_participantes_CSGO')