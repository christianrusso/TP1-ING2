#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmdline.args
import json

from logger.logger import *
from persistencia.lectura import *
from simulacion.simulador_partido import *

ARCHIVO_BASE_DATOS = 'base.db'


def main():
    # Leer argumentos de la línea de comandos.
    arguments = cmdline.args.getArguments([('equipos', 'Un archivo JSON.')])
    
    # Obtener descripciones de los equipos del archivo JSON.
    equipos = []
    with open(arguments['equipos']) as archivoEquipos:
        equipos = json.load(archivoEquipos)
        assert len(equipos) == 2, "Se deben ingresar exactamente dos equipos."
    descripcionPrimerEquipo, descripcionSegundoEquipo = equipos
    
    # Realizar simulación del partido.
    with sqlite3.connect(ARCHIVO_BASE_DATOS) as conexion:
        primerEquipo = construirEquipo(descripcionPrimerEquipo, conexion)
        segundoEquipo = construirEquipo(descripcionSegundoEquipo, conexion)
        logger = Logger()
        simuladorPartido = SimuladorPartido(primerEquipo, segundoEquipo, logger)
        simuladorPartido.simular()


if __name__ == '__main__':
    main()
