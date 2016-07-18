#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from simulador import *
from simulador_turno import *
from resultado_turno import *


class SimuladorPartido(Simulador):
    def __init__(self, primerEquipo, segundoEquipo, logger):
        self.primerEquipo = primerEquipo
        self.segundoEquipo = segundoEquipo
        self.logger = logger
        self.cantidadDeTurnosPorPartido = 40
        self.cantidadDeTurnosPorProrroga = 6
        self.puntajePrimerEquipo, self.puntajeSegundoEquipo = 0, 0
        self.primerEquipoAtacante, self.primerEquipoDefensor = random.choice([
            [self.primerEquipo, self.segundoEquipo],
            [self.segundoEquipo, self.primerEquipo]
        ])

    def simular(self):
        self.registrarComienzoDePartido()
        self.simularTurnos(self.cantidadDeTurnosPorPartido)
        while self.hayEmpate():
            self.simularTurnos(self.cantidadDeTurnosPorProrroga)
        self.registrarFinDePartido()

    def simularTurnos(self, cantidadDeTurnos):
        turnosRestantes = cantidadDeTurnos
        while turnosRestantes > 0:
            turnosRestantes = turnosRestantes - 1
            simuladorTurno = SimuladorTurno(self.primerEquipoAtacante, self.primerEquipoDefensor, self, self.logger)
            resultadoTurno = simuladorTurno.simular()
            resultadoTurno.actualizarSimuladorPartido(self, simuladorTurno)

    def hayEmpate(self):
        return self.puntajePrimerEquipo == self.puntajeSegundoEquipo

    def incrementarPuntaje(self, equipo, cantidadDePuntos):
        if self.primerEquipo == equipo:
            self.puntajePrimerEquipo += cantidadDePuntos
        else:
            self.puntajeSegundoEquipo += cantidadDePuntos

    def invertirRolesEquiposComienzoTurno(self):
        self.primerEquipoAtacante, self.primerEquipoDefensor = self.primerEquipoDefensor, self.primerEquipoAtacante

    def registrarComienzoDePartido(self):
        self.logger.info("Comenzando partido: {primerEquipo} vs {segundoEquipo}.".format(
            primerEquipo= self.primerEquipo.nombre,
            segundoEquipo= self.segundoEquipo.nombre
        ))

    def registrarFinDePartido(self):
        self.logger.info("Fin de partido.")
        self.logger.info("Resultado: {puntajePrimerEquipo} - {puntajeSegundoEquipo}.".format(
            puntajePrimerEquipo= self.puntajePrimerEquipo,
            puntajeSegundoEquipo= self.puntajeSegundoEquipo
        ))
