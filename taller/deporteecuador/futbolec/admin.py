from django.contrib import admin
from .models import Equipo, Jugador, Campeonato, CampeonatoEquipo

# Register your models here.
admin.register(Equipo)
admin.register(Jugador)
admin.register(Campeonato)
admin.register(CampeonatoEquipo)
