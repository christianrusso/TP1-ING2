#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from persistencia.escritura import *

ARCHIVO_BASE_DATOS = 'base.db'

IDS_JUGADORES = [1495, 1626148, 1626156, 200746, 201579, 202695, 203903, 203944, 2225, 2755]

DIRECTORES_TECNICOS = [
    {'idDirectorTecnico': 0, 'nombre': 'Gregg Popovich'},
    {'idDirectorTecnico': 1, 'nombre': 'Byron Scott'},
]

JUGADAS_ATACANTES = [
    {'idDirectorTecnico': 0, 'nombre': 'ColectivaExternaDoble', 'preferencia': 5},
    {'idDirectorTecnico': 0, 'nombre': 'ColectivaExternaTriple', 'preferencia': 5},
    {'idDirectorTecnico': 0, 'nombre': 'MVP', 'preferencia': 5},
    {'idDirectorTecnico': 0, 'nombre': 'Contraataque', 'preferencia': 5},
    {'idDirectorTecnico': 1, 'nombre': 'ColectivaExternaDoble', 'preferencia': 5},
    {'idDirectorTecnico': 1, 'nombre': 'ColectivaExternaTriple', 'preferencia': 5},
    {'idDirectorTecnico': 1, 'nombre': 'MVP', 'preferencia': 5},
    {'idDirectorTecnico': 1, 'nombre': 'Contraataque', 'preferencia': 5},
]

JUGADAS_DEFENSIVAS = [
    {'idDirectorTecnico': 0, 'nombre': 'HombreAHombre', 'preferencia': 5},
    {'idDirectorTecnico': 1, 'nombre': 'HombreAHombre', 'preferencia': 5},
]


def main():
    with sqlite3.connect(ARCHIVO_BASE_DATOS) as conexion:
        crearTablas(conexion)
        print 'Tablas creadas exitosamente.'
        cargarJugadores(IDS_JUGADORES, conexion)
        print 'Jugadores cargados exitosamente.'
        cargarDirectoresTecnicos(DIRECTORES_TECNICOS, conexion)
        print 'DirectoresTecnicos cargados exitosamente.'
        cargarJugadasAtacantes(JUGADAS_ATACANTES, conexion)
        print 'JugadasAtacantes cargadas exitosamente.'
        cargarJugadasDefensivas(JUGADAS_DEFENSIVAS, conexion)
        print 'JugadasDefensivas cargadas exitosamente.'
        conexion.commit()
        print 'Base creada y cargada exitosamente.'


if __name__ == '__main__':
    main()
