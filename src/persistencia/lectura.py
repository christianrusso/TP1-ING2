#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import sqlite3

from simulacion.director_tecnico import *
from simulacion.equipo import *
from simulacion.jugador import *
from simulacion.posicion_jugador import *


def construirEquipo(equipo, conexion):
    nombre = equipo["nombre"]
    idJugadorBase = equipo["base"]
    idJugadorEscolta = equipo["escolta"]
    idJugadorAlero = equipo["alero"]
    idJugadorAlaPivot = equipo["alaPivot"]
    idJugadorPivot = equipo["pivot"]
    idJugadorEstrella = equipo["jugadorEstrella"]
    idDirectorTecnico = equipo["directorTecnico"]
    base = construirJugador(idJugadorBase, PosicionJugadorBase(), conexion)
    escolta = construirJugador(idJugadorEscolta, PosicionJugadorEscolta(), conexion)
    alero = construirJugador(idJugadorAlero, PosicionJugadorAlero(), conexion)
    alaPivot = construirJugador(idJugadorAlaPivot, PosicionJugadorAlaPivot(), conexion)
    pivot = construirJugador(idJugadorPivot, PosicionJugadorPivot(), conexion)
    idJugadores = [idJugadorBase, idJugadorEscolta, idJugadorAlero, idJugadorAlaPivot, idJugadorPivot]
    jugadores = [base, escolta, alero, alaPivot, pivot]
    jugadorEstrella = [jugador for idJugador, jugador in zip(idJugadores, jugadores) if idJugador == idJugadorEstrella][0]
    directorTecnico = construirDirectorTecnico(idDirectorTecnico, conexion)
    return Equipo(nombre, base, escolta, alero, alaPivot, pivot, jugadorEstrella, directorTecnico)
  

def construirJugador(idJugador, posicion, conexion):
    jugador = obtenerJugadorBaseDatos(idJugador, conexion)
    nombre = jugador["nombre"]
    fgp = jugador["FGP"]
    tpp = jugador["TPP"]
    rpg = jugador["RPG"]
    apg = jugador["APG"]
    bpg = jugador["BPG"]
    spg = jugador["SPG"]
    tpg = jugador["TPG"]
    ppg = jugador["PPG"]
    estadisticasJugador = EstadisticasJugador(fgp, tpp, rpg, apg, bpg, spg, tpg, ppg)
    return Jugador(nombre, posicion, estadisticasJugador)


def construirDirectorTecnico(idDirectorTecnico, conexion):
    directorTecnico = obtenerDirectorTecnicoBaseDatos(idDirectorTecnico, conexion)
    nombre = directorTecnico["nombre"]
    nombresJugadasAtacantes = directorTecnico["nombresJugadasAtacantes"]
    nombresJugadasDefensivas = directorTecnico["nombresJugadasDefensivas"]
    preferenciasJugadasAtacantes = directorTecnico["preferenciasJugadasAtacantes"]
    preferenciasJugadasDefensivas = directorTecnico["preferenciasJugadasDefensivas"]
    jugadasAtacantes = map(construirJugadaAtacante, nombresJugadasAtacantes)
    jugadasDefensivas = map(construirJugadaDefensiva, nombresJugadasDefensivas)
    jugadasAtacantesPreferencia = zip(jugadasAtacantes, preferenciasJugadasAtacantes)
    jugadasDefensivasPreferencia = zip(jugadasDefensivas, preferenciasJugadasDefensivas)
    libroJugadas = LibroJugadas(jugadasAtacantesPreferencia, jugadasDefensivasPreferencia)
    return DirectorTecnico(nombre, libroJugadas)

    
def construirJugadaAtacante(nombreJugadaAtacante):
    moduloJugadaAtacante = importlib.import_module("simulacion.jugada_atacante")
    return getattr(moduloJugadaAtacante, "JugadaAtacante{nombre}".format(nombre=nombreJugadaAtacante))()


def construirJugadaDefensiva(nombreJugadaDefensiva):
    moduloJugadaDefensiva = importlib.import_module("simulacion.jugada_defensiva")
    return getattr(moduloJugadaDefensiva, "JugadaDefensiva{nombre}".format(nombre=nombreJugadaDefensiva))()


def obtenerJugadorBaseDatos(idJugador, conexion):
    try:
        consulta = """
            SELECT *
            FROM jugadores
            WHERE idJugador = :idJugador
        """
        filas = hacerConsulta(consulta, {"idJugador": idJugador}, conexion)
        return filas[0]
    except:
        raise RuntimeError("No se pudo cargar el jugador con id = {idJugador}."
                            .format(idJugador=idJugador))


def obtenerDirectorTecnicoBaseDatos(idDirectorTecnico, conexion):
    try:
        consulta = """ 
            SELECT *
            FROM jugadasAtacantes
            WHERE idDirectorTecnico = :idDirectorTecnico
        """
        filas = hacerConsulta(consulta, {'idDirectorTecnico': idDirectorTecnico}, conexion)
        jugadasAtacantes = filas
        consulta = """ 
            SELECT *
            FROM jugadasDefensivas
            WHERE idDirectorTecnico = :idDirectorTecnico
        """
        filas = hacerConsulta(consulta, {'idDirectorTecnico': idDirectorTecnico}, conexion)
        jugadasDefensivas = filas
        consulta = """ 
            SELECT *
            FROM directoresTecnicos
            WHERE idDirectorTecnico = :idDirectorTecnico
        """
        filas = hacerConsulta(consulta, {'idDirectorTecnico': idDirectorTecnico}, conexion)
        directorTecnico = filas[0]
        directorTecnico["nombresJugadasAtacantes"] = map(lambda jugada: jugada["nombre"], jugadasAtacantes)
        directorTecnico["nombresJugadasDefensivas"] = map(lambda jugada: jugada["nombre"], jugadasDefensivas)
        directorTecnico["preferenciasJugadasAtacantes"] = map(lambda jugada: jugada["preferencia"], jugadasAtacantes)
        directorTecnico["preferenciasJugadasDefensivas"] = map(lambda jugada: jugada["preferencia"], jugadasDefensivas)
        return directorTecnico
    except:
        raise RuntimeError("No se pudo cargar el director técnico con id = {idDirectorTecnico}."
                            .format(idDirectorTecnico=idDirectorTecnico))


def hacerConsulta(consulta, argumentos, conexion):
    cursor = conexion.cursor()
    filas = []
    for tupla in cursor.execute(consulta, argumentos):
        fila = {}
        for indice, columna in enumerate(cursor.description):
            fila[columna[0]] = tupla[indice]
        filas.append(fila)
    return filas
