#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulador import *
from simulador_jugada import *
from resultado_jugada import *


class SimuladorTurno(Simulador):
    def __init__(self, primerEquipoAtacante, primerEquipoDefensor, simuladorPartido, logger):
        self.equipoAtacante = primerEquipoAtacante
        self.equipoDefensor = primerEquipoDefensor
        self.simuladorPartido = simuladorPartido
        self.logger = logger
        self.jugadorEmpiezaConPelota = self.equipoAtacante.base
        self.huboRoboPelota = False

    def simular(self):
        self.registrarComienzoDeTurno()
        resultadoJugada = ResultadoJugadaInconcluso()
        while resultadoJugada.turnoEnJuego():
            simuladorJugada = SimuladorJugada(self.jugadorEmpiezaConPelota, self.simuladorPartido, self, self.logger)
            resultadoJugada = simuladorJugada.simular()
            resultadoJugada.actualizarSimuladorTurno(self)
        resultadoTurno = resultadoJugada.obtenerResultadoTurno()
        self.registrarFinDeTurno()
        return resultadoTurno

    def invertirRolesEquipos(self):
        self.equipoAtacante, self.equipoDefensor = self.equipoDefensor, self.equipoAtacante

    def registrarComienzoDeTurno(self):
        self.logger.info("Empezando turno. Equipo empieza atacando: {equipoAtacante}. Equipo empieza defendiendo: {equipoDefensor}.".format(
            equipoAtacante= self.equipoAtacante.nombre,
            equipoDefensor= self.equipoDefensor.nombre
        ))

    def registrarFinDeTurno(self):
        self.logger.info("Terminando turno.")
