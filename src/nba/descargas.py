#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2


def descargarDatosJugador(idJugador):
    informacionBasica = descargarInformacionBasicaNBA(idJugador)
    estadisticas = descargarEstadisticasNBA(idJugador)
    datosDeJugador = {}
    datosDeJugador["nombre"] = informacionBasica["nombre"]
    datosDeJugador["FGP"] = estadisticas["FG_PCT"]
    datosDeJugador["TPP"] = estadisticas["FG3_PCT"]
    datosDeJugador["RPG"] = estadisticas["REB"] / estadisticas["GP"] if estadisticas["GP"] > 0 else 0
    datosDeJugador["APG"] = estadisticas["AST"] / estadisticas["GP"] if estadisticas["GP"] > 0 else 0
    datosDeJugador["BPG"] = estadisticas["BLK"] / estadisticas["GP"] if estadisticas["GP"] > 0 else 0
    datosDeJugador["SPG"] = estadisticas["STL"] / estadisticas["GP"] if estadisticas["GP"] > 0 else 0
    datosDeJugador["TPG"] = estadisticas["TOV"] / estadisticas["GP"] if estadisticas["GP"] > 0 else 0
    datosDeJugador["PPG"] = estadisticas["PTS"] / estadisticas["GP"] if estadisticas["GP"] > 0 else 0
    return datosDeJugador


def descargarInformacionBasicaNBA(idJugador):
    try:
        url = "http://stats.nba.com/stats/commonplayerinfo?PlayerID=%d&LeagueID=00&SeasonType=Regular+Season" % idJugador
        data = consultarApiNBA(url)
        informacionBasica = {}
        for resultSet in data["resultSets"]:
            headers = resultSet["headers"]
            rowSet = resultSet["rowSet"][0]
            if "DISPLAY_FIRST_LAST" in headers:
                informacionBasica["nombre"] = rowSet[headers.index("DISPLAY_FIRST_LAST")]
        assert all(x in informacionBasica for x in ["nombre"])
        return informacionBasica
    except Exception as exception:
        raise RuntimeError("No se pudo obtener la información básica del jugador. Query: " + url + ". Error: " + exception.message)


def descargarEstadisticasNBA(idJugador):
    try:
        url = "http://stats.nba.com/stats/playercareerstats?PlayerID=%d&LeagueID=00&PerMode=PerGame" % idJugador
        data = consultarApiNBA(url)
        estadisticas = {}
        for resultSet in data["resultSets"]:
            if resultSet['name'] == 'CareerTotalsRegularSeason':
                headers = resultSet["headers"]
                rowSet = resultSet["rowSet"][0]
                for (header, value) in zip(headers, rowSet):
                    estadisticas[header] = value
        assert all(x in estadisticas for x in ["FG_PCT", "FG3_PCT", "REB", "AST", "BLK", "STL", "TOV", "PTS", "GP"])
        return estadisticas
    except Exception as exception:
        raise RuntimeError("No se puderion obtener las estadísticas del jugador. Query: " + url + ". Error: " + exception.message)


def consultarApiNBA(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url)
    responseJson = response.read()
    data = json.loads(responseJson)
    return data
