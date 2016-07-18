#!/usr/bin/env python
# -*- coding: utf-8 -*-

from resultado_momento import *


class ResultadoAccionDefensiva():
    def obtenerResultadoMomentoPaseExitoso(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoPaseFallido(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroDobleExitoso(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroDobleFallido(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroTripleExitoso(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroTripleFallido(self, resultadoAccionAtacante):
        raise NotImplementedError()


class ResultadoAccionDefensivaRoboDePaseExitoso(ResultadoAccionDefensiva):
    def __init__(self, accionDefensiva):
        self.accionDefensiva = accionDefensiva

    def obtenerResultadoMomentoPaseExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoPaseRobado(resultadoAccionAtacante, self)

    def obtenerResultadoMomentoPaseFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoPaseRobado(resultadoAccionAtacante, self)

    def obtenerResultadoMomentoTiroDobleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroDobleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroTripleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroTripleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()


class ResultadoAccionDefensivaRoboDePaseFallido(ResultadoAccionDefensiva):
    def __init__(self, accionDefensiva):
        self.accionDefensiva = accionDefensiva

    def obtenerResultadoMomentoPaseExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoPaseExitoso(resultadoAccionAtacante, self)

    def obtenerResultadoMomentoPaseFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaAfuera()

    def obtenerResultadoMomentoTiroDobleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroDobleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroTripleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroTripleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()


class ResultadoAccionDefensiva():
    def obtenerResultadoMomentoPaseExitoso(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoPaseFallido(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroDobleExitoso(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroDobleFallido(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroTripleExitoso(self, resultadoAccionAtacante):
        raise NotImplementedError()

    def obtenerResultadoMomentoTiroTripleFallido(self, resultadoAccionAtacante):
        raise NotImplementedError()


class ResultadoAccionDefensivaBloqueoDeTiroExitoso(ResultadoAccionDefensiva):
    def __init__(self, accionDefensiva):
        self.accionDefensiva = accionDefensiva

    def obtenerResultadoMomentoPaseExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoPaseFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroDobleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaDividida()

    def obtenerResultadoMomentoTiroDobleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaDividida()

    def obtenerResultadoMomentoTiroTripleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaDividida()

    def obtenerResultadoMomentoTiroTripleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaDividida()


class ResultadoAccionDefensivaBloqueoDeTiroFallido(ResultadoAccionDefensiva):
    def __init__(self, accionDefensiva):
        self.accionDefensiva = accionDefensiva

    def obtenerResultadoMomentoPaseExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoPaseFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoInconcluso()

    def obtenerResultadoMomentoTiroDobleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoConversionDoble(resultadoAccionAtacante, self)

    def obtenerResultadoMomentoTiroDobleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaDividida()

    def obtenerResultadoMomentoTiroTripleExitoso(self, resultadoAccionAtacante):
        return ResultadoMomentoConversionTriple(resultadoAccionAtacante, self)

    def obtenerResultadoMomentoTiroTripleFallido(self, resultadoAccionAtacante):
        return ResultadoMomentoPelotaDividida()
