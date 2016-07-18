#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class FormulaResolucionAcciones():
    def evaluar(self, simuladorJugada):
        raise NotImplementedError()


class FormulaAccionAtacantePase(FormulaResolucionAcciones):
    def __init__(self, jugador):
        self.jugador = jugador
        self.estadisticas = jugador.estadisticasJugador

    def evaluar(self, simuladorJugada):
        return 1 - self.estadisticas.tpg * 0.1


class FormulaAccionAtacanteTiroDoble(FormulaResolucionAcciones):
    def __init__(self, jugador):
        self.jugador = jugador
        self.estadisticas = jugador.estadisticasJugador

    def evaluar(self, simuladorJugada):
        bonusApg = min(simuladorJugada.apgAcumulado * 0.025, 0.3)
        return self.estadisticas.fgp + self.estadisticas.ppg * 0.01 + bonusApg


class FormulaAccionAtacanteTiroTriple(FormulaResolucionAcciones):
    def __init__(self, jugador):
        self.jugador = jugador
        self.estadisticas = jugador.estadisticasJugador

    def evaluar(self, simuladorJugada):
        bonusApg = min(simuladorJugada.apgAcumulado * 0.025, 0.3)
        return self.estadisticas.tpp + self.estadisticas.ppg * 0.005 + bonusApg


class FormulaAccionDefensivaRoboDePase(FormulaResolucionAcciones):
    def __init__(self, jugador):
        self.jugador = jugador
        self.estadisticas = jugador.estadisticasJugador

    def evaluar(self, simuladorJugada):
        return self.estadisticas.spg * 0.2


class FormulaAccionDefensivaBloqueoDeTiro(FormulaResolucionAcciones):
    def __init__(self, jugador):
        self.jugador = jugador
        self.estadisticas = jugador.estadisticasJugador

    def evaluar(self, simuladorJugada):
        return self.estadisticas.bpg * 0.2


class FormulaAccionRebote(FormulaResolucionAcciones):
    def __init__(self, jugador):
        self.jugador = jugador
        self.estadisticas = jugador.estadisticasJugador

    def evaluar(self, simuladorJugada):
        return self.estadisticas.rpg * 0.05


class ResolvedorAcciones():
    def __init__(self, formulaResolucionAcciones):
        self.formulaResolucionAcciones = formulaResolucionAcciones

    def resolver(self, accion, simuladorJugada):
        accionExitosa = random.random() < self.formulaResolucionAcciones.evaluar(simuladorJugada)
        return accion.resultadoExitoso if accionExitosa else accion.resultadoFallido

