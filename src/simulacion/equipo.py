#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Equipo():
    def __init__(self, nombre, base, escolta, alero, alaPivot, pivot, jugadorEstrella, directorTecnico):
        self.nombre = nombre
        self.base = base
        self.escolta = escolta
        self.alero = alero
        self.alaPivot = alaPivot
        self.pivot = pivot
        self.jugadorEstrella = jugadorEstrella
        self.directorTecnico = directorTecnico

    def obtenerJugadores(self):
        return [self.base, self.escolta, self.alero, self.alaPivot, self.pivot]

    def obtenerJugadorEnPosicion(self, posicion):
        return posicion.jugadorEnPosicion(self)
