#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import random

from jugada_atacante import *
from jugada_defensiva import *


class DirectorTecnico():
    def __init__(self, nombre, libroJugadas):
        self.nombre = nombre
        self.libroJugadas = libroJugadas
        
    def elegirJugadaAtacante(self, simuladorTurno):
        return self.elegirJugada(self.libroJugadas.jugadasAtacantesPreferencia, simuladorTurno)

    def elegirJugadaDefensiva(self, simuladorTurno):
        return self.elegirJugada(self.libroJugadas.jugadasDefensivasPreferencia, simuladorTurno)

    def elegirJugada(self, jugadasPreferencia, simuladorTurno):
        jugadas = sum([[jugada] * preferencia
                        for jugada, preferencia
                        in jugadasPreferencia
                        if jugada.esAplicable(simuladorTurno)], [])
        return random.choice(jugadas)


class LibroJugadas():
    def __init__(self, jugadasAtacantesPreferencia, jugadasDefensivasPreferencia):
        self.jugadasAtacantesPreferencia = jugadasAtacantesPreferencia
        self.jugadasDefensivasPreferencia = jugadasDefensivasPreferencia
