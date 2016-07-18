#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jugada_defensiva_ejecucion import *


class JugadaDefensiva():
    def esAplicable(self, simuladorTurno):
        raise NotImplementedError()

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        raise NotImplementedError()


class JugadaDefensivaHombreAHombre(JugadaDefensiva):
    def esAplicable(self, simuladorTurno):
        return True

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        return JugadaDefensivaEjecucionHombreAHombre(simuladorTurno, simuladorJugada)
