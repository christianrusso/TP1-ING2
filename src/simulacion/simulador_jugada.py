#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulador import *
from simulador_momento import *
from resultado_momento import *


class SimuladorJugada(Simulador):
    def __init__(self, jugadorEmpiezaConPelota, simuladorPartido, simuladorTurno, logger):
        self.jugadorConPelota = jugadorEmpiezaConPelota
        self.simuladorPartido = simuladorPartido
        self.simuladorTurno = simuladorTurno
        self.logger = logger
        self.jugadaAtacante = simuladorTurno.equipoAtacante.directorTecnico.elegirJugadaAtacante(simuladorTurno)
        self.jugadaDefensiva = simuladorTurno.equipoDefensor.directorTecnico.elegirJugadaDefensiva(simuladorTurno)
        self.jugadaAtacanteEjecucion = self.jugadaAtacante.comenzarJugada(simuladorTurno, self)
        self.jugadaDefensivaEjecucion = self.jugadaDefensiva.comenzarJugada(simuladorTurno, self)
        self.apgAcumulado = 0.0
       
    def simular(self):
        self.registrarComienzoDeJugada()
        resultadoMomento = ResultadoMomentoInconcluso()
        while resultadoMomento.jugadaEnJuego():
            accionAtacante = self.jugadaAtacanteEjecucion.proximaAccion()
            accionDefensiva = self.jugadaDefensivaEjecucion.proximaAccion(accionAtacante)
            simuladorMomento = SimuladorMomento(accionAtacante, accionDefensiva, self.simuladorPartido, self.simuladorTurno, self, self.logger)
            resultadoMomento = simuladorMomento.simular()
            resultadoMomento.actualizarSimuladorJugada(self)
        resultadoJugada = resultadoMomento.obtenerResultadoJugada(self)
        self.registrarFinDeJugada(resultadoJugada)
        return resultadoJugada

    def registrarComienzoDeJugada(self):
        self.logger.info("Empezando jugada. Equipo atacante: {equipoAtacante}. Equipo Defensor: {equipoDefensor}.".format(
            equipoAtacante= self.simuladorTurno.equipoAtacante.nombre,
            equipoDefensor= self.simuladorTurno.equipoDefensor.nombre
        ))
        self.logger.info("Estrategia atacante: {jugadaAtacante}. Estrategia defensiva: {jugadaDefensiva}. Tiene la pelota: {jugadorConPelota}.".format(
            jugadaAtacante= self.jugadaAtacante.__class__.__name__,
            jugadaDefensiva= self.jugadaDefensiva.__class__.__name__,
            jugadorConPelota= self.jugadorConPelota.nombre
        ))

    def registrarPelotaDividida(self):
        self.logger.info("Pelota dividida. Reboteando.")

    def registrarFinDeJugada(self, resultadoJugada):
        self.logger.info("Terminando jugada. Resultado: {resultadoJugada}.".format(
            resultadoJugada= resultadoJugada.__class__.__name__
        ))
