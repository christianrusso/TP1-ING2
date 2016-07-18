#!/usr/bin/env python
# -*- coding: utf-8 -*-

from accion_rebote import *
from resultado_jugada import *


class ResultadoMomento():
    def jugadaEnJuego(self):
        raise NotImplementedError()

    def actualizarSimuladorJugada(self, simuladorJugada):
        raise NotImplementedError()

    def obtenerResultadoJugada(self, simuladorJugada):
        raise NotImplementedError()


class ResultadoMomentoInconcluso(ResultadoMomento):
    def jugadaEnJuego(self):
        return True

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Todavía no terminó el momento, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        return ResultadoJugadaPelotaAfuera()


class ResultadoMomentoConversionDoble(ResultadoMomento):
    def __init__(self, resultadoAccionAtacante, resultadoAccionDefensiva):
        self.resultadoAccionAtacante = resultadoAccionAtacante
        self.resultadoAccionDefensiva = resultadoAccionDefensiva

    def jugadaEnJuego(self):
        return False

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Terminó la jugada, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        return ResultadoJugadaConversionDoble()


class ResultadoMomentoConversionTriple(ResultadoMomento):
    def __init__(self, resultadoAccionAtacante, resultadoAccionDefensiva):
        self.resultadoAccionAtacante = resultadoAccionAtacante
        self.resultadoAccionDefensiva = resultadoAccionDefensiva

    def jugadaEnJuego(self):
        return False

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Terminó la jugada, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        return ResultadoJugadaConversionTriple()


class ResultadoMomentoPaseExitoso(ResultadoMomento):
    def __init__(self, resultadoAccionAtacante, resultadoAccionDefensiva):
        self.resultadoAccionAtacante = resultadoAccionAtacante
        self.resultadoAccionDefensiva = resultadoAccionDefensiva

    def jugadaEnJuego(self):
        return True

    def actualizarSimuladorJugada(self, simuladorJugada):
        accionAtacante = self.resultadoAccionAtacante.accionAtacante
        jugadorHizoPase = accionAtacante.jugadorConPelota
        jugadorReceptor = accionAtacante.jugadorReceptor
        simuladorJugada.jugadorConPelota = jugadorReceptor
        simuladorJugada.apgAcumulado = simuladorJugada.apgAcumulado + jugadorHizoPase.estadisticasJugador.apg


class ResultadoMomentoPelotaDividida(ResultadoMomento):
    def jugadaEnJuego(self):
        return False

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Terminó la jugada, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        simuladorJugada.registrarPelotaDividida()
        simuladorTurno = simuladorJugada.simuladorTurno
        defensores = simuladorTurno.equipoDefensor.obtenerJugadores()
        atacantes = simuladorTurno.equipoAtacante.obtenerJugadores()
        defensoresEquipo = zip(defensores, [simuladorTurno.equipoDefensor] * len(defensores))
        atacantesEquipo = zip(atacantes, [simuladorTurno.equipoAtacante] * len(atacantes))
        jugadoresEquipo = [jugadorEquipo for par in zip(defensoresEquipo, atacantesEquipo) for jugadorEquipo in par]
        indiceJugadores, resultadoMomento = 0, ResultadoMomentoInconcluso()
        while indiceJugadores < len(jugadoresEquipo) and resultadoMomento.jugadaEnJuego():
            jugador, equipo = jugadoresEquipo[indiceJugadores]
            resultadoAccionRebote = AccionRebote(jugador, equipo).obtenerResultado(simuladorJugada)
            resultadoMomento = resultadoAccionRebote.obtenerResultadoMomento()
            indiceJugadores = indiceJugadores + 1
        return resultadoMomento.obtenerResultadoJugada(simuladorJugada)


class ResultadoMomentoPelotaRecuperada(ResultadoMomento):
    def __init__(self, resultadoAccionRebote):
        self.resultadoAccionRebote = resultadoAccionRebote

    def jugadaEnJuego(self):
        return False

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Terminó la jugada, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        return ResultadoJugadaPelotaRecuperada(self)


class ResultadoMomentoPaseRobado(ResultadoMomento):
    def __init__(self, resultadoAccionAtacante, resultadoAccionDefensiva):
        self.resultadoAccionAtacante = resultadoAccionAtacante
        self.resultadoAccionDefensiva = resultadoAccionDefensiva

    def jugadaEnJuego(self):
        return False

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Terminó la jugada, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        return ResultadoJugadaPaseRobado(self)


class ResultadoMomentoPelotaAfuera(ResultadoMomento):
    def jugadaEnJuego(self):
        return False

    def actualizarSimuladorJugada(self, simuladorJugada):
        pass # Terminó la jugada, no hago nada.

    def obtenerResultadoJugada(self, simuladorJugada):
        return ResultadoJugadaPelotaAfuera()
