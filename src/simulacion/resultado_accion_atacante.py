#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ResultadoAccionAtacante():
    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        raise NotImplementedError()


class ResultadoAccionAtacanteTiroDobleExitoso(ResultadoAccionAtacante):
    def __init__(self, accionAtacante):
        self.accionAtacante = accionAtacante

    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        return resultadoAccionDefensiva.obtenerResultadoMomentoTiroDobleExitoso(self)


class ResultadoAccionAtacanteTiroDobleFallido(ResultadoAccionAtacante):
    def __init__(self, accionAtacante):
        self.accionAtacante = accionAtacante

    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        return resultadoAccionDefensiva.obtenerResultadoMomentoTiroDobleFallido(self)


class ResultadoAccionAtacanteTiroTripleExitoso(ResultadoAccionAtacante):
    def __init__(self, accionAtacante):
        self.accionAtacante = accionAtacante

    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        return resultadoAccionDefensiva.obtenerResultadoMomentoTiroTripleExitoso(self)


class ResultadoAccionAtacanteTiroTripleFallido(ResultadoAccionAtacante):
    def __init__(self, accionAtacante):
        self.accionAtacante = accionAtacante

    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        return resultadoAccionDefensiva.obtenerResultadoMomentoTiroTripleFallido(self)


class ResultadoAccionAtacantePaseExitoso(ResultadoAccionAtacante):
    def __init__(self, accionAtacante):
        self.accionAtacante = accionAtacante

    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        return resultadoAccionDefensiva.obtenerResultadoMomentoPaseExitoso(self)


class ResultadoAccionAtacantePaseFallido(ResultadoAccionAtacante):
    def __init__(self, accionAtacante):
        self.accionAtacante = accionAtacante

    def obtenerResultadoMomento(self, resultadoAccionDefensiva):
        return resultadoAccionDefensiva.obtenerResultadoMomentoPaseFallido(self)
