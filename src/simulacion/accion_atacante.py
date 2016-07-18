#!/usr/bin/env python
# -*- coding: utf-8 -*-

from accion_defensiva import *
from formula_resolucion_acciones import *
from resultado_accion_atacante import *


class AccionAtacante():
    def obtenerResultado(self, simuladorJugada):
        raise NotImplementedError()

    def obtenerAccionDefensiva(self, defensor):
        raise NotImplementedError()


class AccionAtacantePase(AccionAtacante):
    def __init__(self, jugadorConPelota, jugadorReceptor):
        self.jugadorConPelota = jugadorConPelota
        self.jugadorReceptor = jugadorReceptor
        self.resultadoExitoso = ResultadoAccionAtacantePaseExitoso(self)
        self.resultadoFallido = ResultadoAccionAtacantePaseFallido(self)
        self.resolvedorAcciones = ResolvedorAcciones(FormulaAccionAtacantePase(jugadorConPelota))

    def obtenerResultado(self, simuladorJugada):
        return self.resolvedorAcciones.resolver(self, simuladorJugada)
    
    def obtenerAccionDefensiva(self, defensor):
        return AccionDefensivaRoboDePase(defensor)


class AccionAtacanteTiroDoble(AccionAtacante):
    def __init__(self, jugadorConPelota):
        self.jugadorConPelota = jugadorConPelota
        self.resultadoExitoso = ResultadoAccionAtacanteTiroDobleExitoso(self)
        self.resultadoFallido = ResultadoAccionAtacanteTiroDobleFallido(self)
        self.resolvedorAcciones = ResolvedorAcciones(FormulaAccionAtacanteTiroDoble(jugadorConPelota))

    def obtenerResultado(self, simuladorJugada):
        return self.resolvedorAcciones.resolver(self, simuladorJugada)
    
    def obtenerAccionDefensiva(self, defensor):
        return AccionDefensivaBloqueoDeTiro(defensor)


class AccionAtacanteTiroTriple(AccionAtacante):
    def __init__(self, jugadorConPelota):
        self.jugadorConPelota = jugadorConPelota
        self.resultadoExitoso = ResultadoAccionAtacanteTiroTripleExitoso(self)
        self.resultadoFallido = ResultadoAccionAtacanteTiroTripleFallido(self)
        self.resolvedorAcciones = ResolvedorAcciones(FormulaAccionAtacanteTiroTriple(jugadorConPelota))

    def obtenerResultado(self, simuladorJugada):
        return self.resolvedorAcciones.resolver(self, simuladorJugada)

    def obtenerAccionDefensiva(self, defensor):
        return AccionDefensivaBloqueoDeTiro(defensor)
