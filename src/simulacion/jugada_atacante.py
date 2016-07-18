#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jugada_atacante_ejecucion import *


class JugadaAtacante():
    def esAplicable(self, simuladorTurno):
        raise NotImplementedError()

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        raise NotImplementedError()


class JugadaAtacanteColectivaExternaDoble(JugadaAtacante):
    def esAplicable(self, simuladorTurno):
        return True

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        return JugadaAtacanteEjecucionColectivaExternaDoble(simuladorTurno, simuladorJugada)


class JugadaAtacanteColectivaExternaTriple(JugadaAtacante):
    def esAplicable(self, simuladorTurno):
        return True

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        return JugadaAtacanteEjecucionColectivaExternaTriple(simuladorTurno, simuladorJugada)


class JugadaAtacanteMVP(JugadaAtacante):
    def esAplicable(self, simuladorTurno):
        return True

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        return JugadaAtacanteEjecucionMVP(simuladorTurno, simuladorJugada)


class JugadaAtacanteContraataque(JugadaAtacante):
    def esAplicable(self, simuladorTurno):
        return simuladorTurno.huboRoboPelota

    def comenzarJugada(self, simuladorTurno, simuladorJugada):
        return JugadaAtacanteEjecucionContraataque(simuladorTurno, simuladorJugada)
