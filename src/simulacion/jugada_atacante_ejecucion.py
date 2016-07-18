#!/usr/bin/env python
# -*- coding: utf-8 -*-

from accion_atacante import *


class JugadaAtacanteEjecucion():
    def proximaAccion(self):
        raise NotImplementedError()


class JugadaAtacanteEjecucionColectivaExternaDoble(JugadaAtacanteEjecucion):
    def __init__(self, simuladorTurno, simuladorJugada):
        self.simuladorTurno = simuladorTurno
        self.simuladorJugada = simuladorJugada
        self.cantidadDePasesTotal = 2
        self.cantidadDePasesRealizados = 0

    def proximaAccion(self):
        jugadorConPelota = self.simuladorJugada.jugadorConPelota
        while self.cantidadDePasesRealizados < self.cantidadDePasesTotal:
            self.cantidadDePasesRealizados = self.cantidadDePasesRealizados + 1
            return AccionAtacantePase(jugadorConPelota, jugadorConPelota)
        return AccionAtacanteTiroDoble(jugadorConPelota)


class JugadaAtacanteEjecucionColectivaExternaTriple(JugadaAtacanteEjecucion):
    def __init__(self, simuladorTurno, simuladorJugada):
        self.simuladorTurno = simuladorTurno
        self.simuladorJugada = simuladorJugada
        self.cantidadDePasesTotal = 2
        self.cantidadDePasesRealizados = 0

    def proximaAccion(self):
        jugadorConPelota = self.simuladorJugada.jugadorConPelota
        while self.cantidadDePasesRealizados < self.cantidadDePasesTotal:
            self.cantidadDePasesRealizados = self.cantidadDePasesRealizados + 1
            return AccionAtacantePase(jugadorConPelota, jugadorConPelota)
        return AccionAtacanteTiroTriple(jugadorConPelota)


class JugadaAtacanteEjecucionMVP(JugadaAtacanteEjecucion):
    def __init__(self, simuladorTurno, simuladorJugada):
        self.simuladorTurno = simuladorTurno
        self.simuladorJugada = simuladorJugada

    def proximaAccion(self):
        jugadorConPelota = self.simuladorJugada.jugadorConPelota
        jugadorEstrella = self.simuladorTurno.equipoAtacante.jugadorEstrella
        while self.simuladorJugada.jugadorConPelota != jugadorEstrella:
            return AccionAtacantePase(jugadorConPelota, jugadorConPelota)
        return AccionAtacanteTiroTriple(jugadorConPelota)


class JugadaAtacanteEjecucionContraataque(JugadaAtacanteEjecucion):
    def __init__(self, simuladorTurno, simuladorJugada):
        self.simuladorTurno = simuladorTurno
        self.simuladorJugada = simuladorJugada

    def proximaAccion(self):
        jugadorConPelota = self.simuladorJugada.jugadorConPelota
        return AccionAtacanteTiroTriple(jugadorConPelota)
