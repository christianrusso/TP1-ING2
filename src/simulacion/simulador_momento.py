#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulador import *


class SimuladorMomento(Simulador):
    def __init__(self, accionAtacante, accionDefensiva, simuladorPartido, simuladorTurno, simuladorJugada, logger):
        self.accionAtacante = accionAtacante
        self.accionDefensiva = accionDefensiva
        self.simuladorPartido = simuladorPartido
        self.simuladorTurno = simuladorTurno
        self.simuladorJugada = simuladorJugada
        self.logger = logger
       
    def simular(self):
        self.registrarComienzoDeMomento()
        resultadoAccionAtacante = self.accionAtacante.obtenerResultado(self.simuladorJugada)
        resultadoAccionDefensiva = self.accionDefensiva.obtenerResultado(self.simuladorJugada)
        resultadoMomento = resultadoAccionAtacante.obtenerResultadoMomento(resultadoAccionDefensiva)
        self.registrarFinDeMomento(resultadoMomento)
        return resultadoMomento

    def registrarComienzoDeMomento(self):
        self.logger.info("Empezando momento. Accion atacante: {accionAtacante}. Accion defensiva: {accionDefensiva}.".format(
            accionAtacante= self.accionAtacante.__class__.__name__,
            accionDefensiva= self.accionDefensiva.__class__.__name__
        ))

    def registrarFinDeMomento(self, resultadoMomento):
        self.logger.info("Terminando momento. Resultado: {resultadoMomento}.".format(
            resultadoMomento= resultadoMomento.__class__.__name__
        ))
