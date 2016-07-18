#!/usr/bin/env python
# -*- coding: utf-8 -*-

import resultado_momento


class ResultadoAccionRebote():
    def obtenerResultadoMomento(self):
        raise NotImplementedError()


class ResultadoAccionReboteExitoso():
    def __init__(self, accionRebote):
        self.accionRebote = accionRebote

    def obtenerResultadoMomento(self):
        return resultado_momento.ResultadoMomentoPelotaRecuperada(self)


class ResultadoAccionReboteFallido():
    def __init__(self, accionRebote):
        self.accionRebote = accionRebote

    def obtenerResultadoMomento(self):
        return resultado_momento.ResultadoMomentoInconcluso() 
