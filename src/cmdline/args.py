#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys


def getArguments(arguments):
    argumentParser = argparse.ArgumentParser(prog= sys.argv[0])
    for argumentName, argumentHelp in arguments:
        argumentParser.add_argument('--{argumentName}'.format(argumentName= argumentName),
                                    help= argumentHelp,
                                    required= True)
    return vars(argumentParser.parse_args(sys.argv[1:]))
