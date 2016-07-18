#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PosicionJugador():
    def jugadorEnPosicion(self, equipo):
        raise NotImplementedError()


class PosicionJugadorBase(PosicionJugador):
    def jugadorEnPosicion(self, equipo):
        return equipo.base


class PosicionJugadorEscolta(PosicionJugador):
    def jugadorEnPosicion(self, equipo):
        return equipo.escolta


class PosicionJugadorAlero(PosicionJugador):
    def jugadorEnPosicion(self, equipo):
        return equipo.alero


class PosicionJugadorAlaPivot(PosicionJugador):
    def jugadorEnPosicion(self, equipo):
        return equipo.alaPivot


class PosicionJugadorPivot(PosicionJugador):
    def jugadorEnPosicion(self, equipo):
        return equipo.pivot
