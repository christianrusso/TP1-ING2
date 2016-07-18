#!/usr/bin/env python
# -*- coding: utf-8 -*-

from formula_resolucion_acciones import *
from resultado_accion_defensiva import *


class AccionDefensiva():
    def obtenerResultado(self, simuladorJugada):
        raise NotImplementedError()


class AccionDefensivaRoboDePase(AccionDefensiva):
    def __init__(self, defensor):
        self.defensor = defensor
        self.resultadoExitoso = ResultadoAccionDefensivaRoboDePaseExitoso(self)
        self.resultadoFallido = ResultadoAccionDefensivaRoboDePaseFallido(self)
        self.resolvedorAcciones = ResolvedorAcciones(FormulaAccionDefensivaRoboDePase(defensor))

    def obtenerResultado(self, simuladorJugada):
        return self.resolvedorAcciones.resolver(self, simuladorJugada)


class AccionDefensivaBloqueoDeTiro(AccionDefensiva):
    def __init__(self, defensor):
        self.defensor = defensor
        self.resultadoExitoso = ResultadoAccionDefensivaBloqueoDeTiroExitoso(self)
        self.resultadoFallido = ResultadoAccionDefensivaBloqueoDeTiroFallido(self)
        self.resolvedorAcciones = ResolvedorAcciones(FormulaAccionDefensivaBloqueoDeTiro(defensor))

    def obtenerResultado(self, simuladorJugada):
        return self.resolvedorAcciones.resolver(self, simuladorJugada)
