#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nba.descargas import *


def crearTablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores(idJugador integer, nombre text,
                FGP real, TPP real, RPG real, APG real, BPG real, SPG real, TPG real, PPG real,
        PRIMARY KEY(idJugador))
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS directoresTecnicos(idDirectorTecnico integer, nombre text,
        PRIMARY KEY(idDirectorTecnico))
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadasAtacantes(idDirectorTecnico integer, nombre text, preferencia integer,
        PRIMARY KEY(idDirectorTecnico, nombre))
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadasDefensivas(idDirectorTecnico integer, nombre text, preferencia integer,
        PRIMARY KEY(idDirectorTecnico, nombre))
    """)


def cargarJugadores(idJugadores, conexion):
    cursor = conexion.cursor()
    comando = "INSERT OR REPLACE INTO jugadores VALUES (?,?,?,?,?,?,?,?,?,?)"
    for idJugador in idJugadores:
        datosDeJugador = descargarDatosJugador(idJugador)
        fila = [
            idJugador,
            datosDeJugador["nombre"],
            datosDeJugador["FGP"],
            datosDeJugador["TPP"],
            datosDeJugador["RPG"],
            datosDeJugador["APG"],
            datosDeJugador["BPG"],
            datosDeJugador["SPG"],
            datosDeJugador["TPG"],
            datosDeJugador["PPG"],
        ]
        cursor.execute(comando, fila)


def cargarDirectoresTecnicos(directoresTecnicos, conexion):
    cursor = conexion.cursor()
    comando = "INSERT OR REPLACE INTO directoresTecnicos VALUES (?, ?)"
    for directorTecnico in directoresTecnicos:
        fila = [
            directorTecnico['idDirectorTecnico'],
            directorTecnico['nombre'],
        ]
        cursor.execute(comando, fila)


def cargarJugadasAtacantes(jugadasAtacantes, conexion):
    cursor = conexion.cursor()
    comando = "INSERT OR REPLACE INTO jugadasAtacantes VALUES (?, ?, ?)"
    for jugadaAtacante in jugadasAtacantes:
        fila = [
            jugadaAtacante['idDirectorTecnico'],
            jugadaAtacante['nombre'],
            jugadaAtacante['preferencia'],
        ]
        cursor.execute(comando, fila)


def cargarJugadasDefensivas(jugadasDefensivas, conexion):
    cursor = conexion.cursor()
    comando = "INSERT OR REPLACE INTO jugadasDefensivas VALUES (?, ?, ?)"
    for jugadaDefensiva in jugadasDefensivas:
        fila = [
            jugadaDefensiva['idDirectorTecnico'],
            jugadaDefensiva['nombre'],
            jugadaDefensiva['preferencia'],
        ]
        cursor.execute(comando, fila)

