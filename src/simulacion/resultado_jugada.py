#!/usr/bin/env python
# -*- coding: utf-8 -*-

from resultado_turno import *


class ResultadoJugada():
    def turnoEnJuego(self):
        raise NotImplementedError()

    def actualizarSimuladorTurno(self, simuladorTurno):
        raise NotImplementedError()
    
    def obtenerResultadoTurno(self):
        raise NotImplementedError()


class ResultadoJugadaInconcluso(ResultadoJugada):
    def turnoEnJuego(self):
        return True

    def actualizarSimuladorTurno(self, simuladorTurno):
        pass # Todavía no terminó la jugada, no hago nada.


class ResultadoJugadaConversionDoble(ResultadoJugada):
    def turnoEnJuego(self):
        return False

    def actualizarSimuladorTurno(self, simuladorTurno):
        pass # Terminó el turno, no hago nada.

    def obtenerResultadoTurno(self):
        return ResultadoTurnoConversionDoble()


class ResultadoJugadaConversionTriple(ResultadoJugada):
    def turnoEnJuego(self):
        return False

    def actualizarSimuladorTurno(self, simuladorTurno):
        pass # Terminó el turno, no hago nada.

    def obtenerResultadoTurno(self):
        return ResultadoTurnoConversionTriple()


class ResultadoJugadaPelotaRecuperada(ResultadoJugada):
    def __init__(self, resultadoMomento):
        self.resultadoMomento = resultadoMomento

    def turnoEnJuego(self):
        return True

    def actualizarSimuladorTurno(self, simuladorTurno):
        jugador = self.resultadoMomento.resultadoAccionRebote.accionRebote.jugador
        equipo = self.resultadoMomento.resultadoAccionRebote.accionRebote.equipo
        while simuladorTurno.equipoAtacante != equipo:
            simuladorTurno.invertirRolesEquipos()
        simuladorTurno.jugadorEmpiezaConPelota = jugador
        simuladorTurno.huboRoboPelota = False


class ResultadoJugadaPaseRobado(ResultadoJugada):
    def __init__(self, resultadoMomento):
        self.resultadoMomento = resultadoMomento

    def turnoEnJuego(self):
        return True

    def actualizarSimuladorTurno(self, simuladorTurno):
        defensor = self.resultadoMomento.resultadoAccionDefensiva.accionDefensiva.defensor
        simuladorTurno.invertirRolesEquipos()
        simuladorTurno.jugadorEmpiezaConPelota = defensor
        simuladorTurno.huboRoboPelota = True


class ResultadoJugadaPelotaAfuera(ResultadoJugada):
    def turnoEnJuego(self):
        return False

    def actualizarSimuladorTurno(self, simuladorTurno):
        pass # Terminó el turno, no hago nada.

    def obtenerResultadoTurno(self):
        return ResultadoTurnoPelotaAfuera()
