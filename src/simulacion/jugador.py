#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Jugador():
    def __init__(self, nombre, posicion, estadisticasJugador):
        self.nombre = nombre
        self.posicion = posicion
        self.estadisticasJugador = estadisticasJugador


class EstadisticasJugador():
    def __init__(self, fgp, tpp, rpg, apg, bpg, spg, tpg, ppg):
        self.fgp = fgp
        self.tpp = tpp  #3p%
        self.rpg = rpg
        self.apg = apg
        self.bpg = bpg
        self.spg = spg
        self.tpg = tpg  #to
        self.ppg = ppg
