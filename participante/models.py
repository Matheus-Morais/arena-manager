from django.db import models

# Create your models here.

class Participante(models.Model):
    JOGO_CHOICES = (
        ('LOL', 'League of Legends'),
        ('FIFA', 'FIFA'),
        ('CSGO', 'CS:GO'),
    )

    nome = models.CharField(max_length=200, verbose_name='Nome')
    jogo = models.CharField(verbose_name='Jogo', max_length=4, choices=JOGO_CHOICES)
    vitoria = models.IntegerField(verbose_name='Vitorias', default=0)
    derrota = models.IntegerField(verbose_name='Derrotas', default=0)
    empate = models.IntegerField(verbose_name='Empates', default=0)

    def __str__(self):
        return self.nome

class Partida(models.Model):
    DIA_CHOICES = (
        ('T', 'Terça-feira'),
        ('Q', 'Quarta-feira'),
        ('QI', 'Quinta-feira'),
        ('S', 'Sexta-feira'),
    )

    JOGO_CHOICES = (
        ('LOL', 'League of Legends'),
        ('FIFA', 'FIFA'),
        ('CSGO', 'CS:GO'),
    )

    jogo = models.CharField(verbose_name='Jogo', max_length=4, choices=JOGO_CHOICES)
    dia = models.CharField(verbose_name='Dia', max_length=2, choices=DIA_CHOICES)
    participante_casa = models.ForeignKey(Participante, related_name='participante_casa', on_delete=models.PROTECT)
    participante_desafiante = models.ForeignKey(Participante, related_name='participante_desafiante', on_delete=models.PROTECT)

    def __str__(self):
        return self.participante_casa.nome + ' VS ' + self.participante_desafiante.nome