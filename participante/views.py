from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def lista_participantes_partidas_lol(request):
    participantes = Participante.objects.filter(jogo = 'LOL')
    partidas_terca = Partida.objects.filter(jogo = 'LOL', dia = 'T')
    partidas_quarta = Partida.objects.filter(jogo = 'LOL', dia = 'Q')
    partidas_quinta = Partida.objects.filter(jogo = 'LOL', dia = 'QI')
    partidas_sexta = Partida.objects.filter(jogo = 'LOL', dia = 'S')
    return render(request, 'participantes/lista_participantes_partidas_lol.html', {'participantes': participantes, 'partidas_terca': partidas_terca, 'partidas_quarta':partidas_quarta, 'partidas_quinta':partidas_quinta, 'partidas_sexta':partidas_sexta})

@login_required
def lista_participantes_partidas_fifa(request):
    participantes = Participante.objects.filter(jogo = 'FIFA')
    partidas_terca = Partida.objects.filter(jogo = 'FIFA', dia = 'T')
    partidas_quarta = Partida.objects.filter(jogo = 'FIFA', dia = 'Q')
    partidas_quinta = Partida.objects.filter(jogo = 'FIFA', dia = 'QI')
    partidas_sexta = Partida.objects.filter(jogo = 'FIFA', dia = 'S')
    return render(request, 'participantes/lista_participantes_partidas_fifa.html', {'participantes': participantes, 'partidas_terca': partidas_terca, 'partidas_quarta':partidas_quarta, 'partidas_quinta':partidas_quinta, 'partidas_sexta':partidas_sexta})

@login_required
def lista_participantes_partidas_cs(request):
    participantes = Participante.objects.filter(jogo = 'CSGO')
    partidas_terca = Partida.objects.filter(jogo = 'CSGO', dia = 'T')
    partidas_quarta = Partida.objects.filter(jogo = 'CSGO', dia = 'Q')
    partidas_quinta = Partida.objects.filter(jogo = 'CSGO', dia = 'QI')
    partidas_sexta = Partida.objects.filter(jogo = 'CSGO', dia = 'S')
    return render(request, 'participantes/lista_participantes_partidas_csgo.html', {'participantes': participantes, 'partidas_terca': partidas_terca, 'partidas_quarta':partidas_quarta, 'partidas_quinta':partidas_quinta, 'partidas_sexta':partidas_sexta})

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
                return redirect('participantes:lista-participantes-partidas-LOL')
            elif participante.jogo == 'FIFA':
                return redirect('participantes:lista-participantes-partidas-FIFA')
            elif participante.jogo == 'CSGO':
                return redirect('participantes:lista-participantes-partidas-CSGO')
    else:
        form = ParticipanteForms(instance=participante)
        return render(request, 'participantes/novo_participante.html', {'form': form})

@login_required
def excluir_participante(request, id):
    participante = Participante.objects.get(pk=id)
    participante.delete()
    if participante.jogo == 'LOL':
        return redirect('participantes:lista-participantes-partidas-LOL')
    elif participante.jogo == 'FIFA':
        return redirect('participantes:lista-participantes-partidas-FIFA')
    elif participante.jogo == 'CSGO':
        return redirect('participantes:lista-participantes-partidas-CSGO')

@login_required
def nova_partida_lol(request):
    if request.method == 'POST':
        form = PartidaLOLForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('participantes:nova-partida-lol')
        else:
            print(form.errors)
    else:
        form = PartidaLOLForms()
    return render(request, 'partidas/nova_partida.html', {'form': form})

@login_required
def nova_partida_fifa(request):
    if request.method == 'POST':
        form = PartidaFIFAForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('participantes:nova-partida-fifa')
        else:
            print(form.errors)
    else:
        form = PartidaFIFAForms()
    return render(request, 'partidas/nova_partida.html', {'form': form})

@login_required
def nova_partida_csgo(request):
    if request.method == 'POST':
        form = PartidaCSGOForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('participantes:nova-partida-csgo')
        else:
            print(form.errors)
    else:
        form = PartidaCSGOForms()
    return render(request, 'partidas/nova_partida.html', {'form': form})

@login_required
def editar_partida(request, id):
    partida = get_object_or_404(Partida, id=id)
    if request.method == 'POST':
        if partida.jogo == 'LOL':
            form = PartidaLOLForms(request.POST, instance=partida)
        elif partida.jogo == 'FIFA':
            form = PartidaFIFAForms(request.POST, instance=partida)
        elif partida.jogo == 'CSGO':
            form = PartidaCSGOForms(request.POST, instance=partida)
        
        if form.is_valid():
            form.save()
            if partida.jogo == 'LOL':
                casa = Participante.objects.get(pk = partida.participante_casa.id)
                desafiante = Participante.objects.get(pk = partida.participante_desafiante.id)

                if (partida.vencedor == 'C'):
                    casa.vitoria = casa.vitoria + 1
                    casa.save()
                    desafiante.derrota = casa.derrota + 1
                    desafiante.save()

                elif (partida.vencedor == 'D'):
                    casa.derrota = casa.derrota + 1
                    casa.save()
                    desafiante.vitoria = casa.vitoria + 1
                    desafiante.save()

                elif (partida.vencedor == 'E'):
                    casa.empate = casa.empate + 1
                    casa.save()
                    desafiante.empate = desafiante.empate + 1
                    desafiante.save()

                return redirect('participantes:lista-participantes-partidas-LOL')
            elif partida.jogo == 'FIFA':
                casa = Participante.objects.get(pk = partida.participante_casa.id)
                desafiante = Participante.objects.get(pk = partida.participante_desafiante.id)

                if (partida.vencedor == 'C'):
                    casa.vitoria = casa.vitoria + 1
                    casa.save()
                    desafiante.derrota = casa.derrota + 1
                    desafiante.save()

                elif (partida.vencedor == 'D'):
                    casa.derrota = casa.derrota + 1
                    casa.save()
                    desafiante.vitoria = casa.vitoria + 1
                    desafiante.save()

                elif (partida.vencedor == 'E'):
                    casa.empate = casa.empate + 1
                    casa.save()
                    desafiante.empate = desafiante.empate + 1
                    desafiante.save()

                return redirect('participantes:lista-participantes-partidas-FIFA')
            elif partida.jogo == 'CSGO':
                casa = Participante.objects.get(pk = partida.participante_casa.id)
                desafiante = Participante.objects.get(pk = partida.participante_desafiante.id)

                if (partida.vencedor == 'C'):
                    casa.vitoria = casa.vitoria + 1
                    casa.save()
                    desafiante.derrota = casa.derrota + 1
                    desafiante.save()

                elif (partida.vencedor == 'D'):
                    casa.derrota = casa.derrota + 1
                    casa.save()
                    desafiante.vitoria = casa.vitoria + 1
                    desafiante.save()

                elif (partida.vencedor == 'E'):
                    casa.empate = casa.empate + 1
                    casa.save()
                    desafiante.empate = desafiante.empate + 1
                    desafiante.save()

                return redirect('participantes:lista-participantes-partidas-CSGO')
    else:
        form = PartidaForms(instance=partida)
        return render(request, 'partidas/nova_partida.html', {'form': form})

@login_required
def excluir_partida(request, id):
    partida = Partida.objects.get(pk=id)
    partida.delete()
    if partida.jogo == 'LOL':
        return redirect('participantes:lista-participantes-partidas-LOL')
    elif partida.jogo == 'FIFA':
        return redirect('participantes:lista-participantes-partidas-FIFA')
    elif partida.jogo == 'CSGO':
        return redirect('participantes:lista-participantes-partidas-CSGO')

