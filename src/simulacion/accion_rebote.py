#!/usr/bin/env python
# -*- coding: utf-8 -*-

from formula_resolucion_acciones import *
from resultado_accion_rebote import *


class AccionRebote():
    def __init__(self, jugador, equipo):
        self.jugador = jugador
        self.equipo = equipo
        self.resultadoExitoso = ResultadoAccionReboteExitoso(self)
        self.resultadoFallido = ResultadoAccionReboteFallido(self)
        self.resolvedorAcciones = ResolvedorAcciones(FormulaAccionRebote(jugador))

    def obtenerResultado(self, simuladorJugada):
        return self.resolvedorAcciones.resolver(self, simuladorJugada)
