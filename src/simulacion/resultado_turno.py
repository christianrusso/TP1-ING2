#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ResultadoTurno():
    def actualizarSimuladorPartido(self, simuladorPartido, simuladorTurno):
        raise NotImplementedError()


class ResultadoTurnoInconcluso(ResultadoTurno):
    def actualizarSimuladorPartido(self, simuladorPartido, simuladorTurno):
        pass # Todavía no terminó el turno, no hago nada.


class ResultadoTurnoConversionDoble(ResultadoTurno):
    def actualizarSimuladorPartido(self, simuladorPartido, simuladorTurno):
        simuladorPartido.incrementarPuntaje(simuladorTurno.equipoAtacante, 2)
        simuladorPartido.invertirRolesEquiposComienzoTurno()


class ResultadoTurnoConversionTriple(ResultadoTurno):
    def actualizarSimuladorPartido(self, simuladorPartido, simuladorTurno):
        simuladorPartido.incrementarPuntaje(simuladorTurno.equipoAtacante, 3)
        simuladorPartido.invertirRolesEquiposComienzoTurno()


class ResultadoTurnoPelotaAfuera(ResultadoTurno):
    def actualizarSimuladorPartido(self, simuladorPartido, simuladorTurno):
        simuladorPartido.invertirRolesEquiposComienzoTurno()
