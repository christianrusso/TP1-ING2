#!/usr/bin/env python
# -*- coding: utf-8 -*-


class JugadaDefensivaEjecucion():
    def proximaAccion(self, accionAtacante):
        raise NotImplementedError()


class JugadaDefensivaEjecucionHombreAHombre(JugadaDefensivaEjecucion):
    def __init__(self, simuladorTurno, simuladorJugada):
        self.simuladorTurno = simuladorTurno
        self.simuladorJugada = simuladorJugada

    def proximaAccion(self, accionAtacante):
        posicionJugador = accionAtacante.jugadorConPelota.posicion
        defensor = self.simuladorTurno.equipoDefensor.obtenerJugadorEnPosicion(posicionJugador)
        return accionAtacante.obtenerAccionDefensiva(defensor)
