#!/usr/bin/env python
# python

# REQUIRED BUILT-IN MODULES
import numpy as np
import itertools
import os
import sys
import string

import memo2gral.globals as cfg

###############################
# Module to import and create #
# basic input files           #
###############################
# A. Berchet - Feb. 2016
# K. Zink    - Feb. 2016

############################################################################
# Read the config file
############################################################################


def ReadConfig(config):

    print("##################")
    print("Preparing GRAL input files from the config folder:")
    print(config)
    print("##################\n\n\n")

    if not os.path.isdir(config):

        print("WARNING! I can't find the configuration directory for GRAL.")
        print("Please be sure that it exists")

    else:

        ReadDom(config)

        # ReadInputs(config)

        # ReadOutputs(config)

        # ReadRun(config)

        # ReadVisualize(config)

        # InitGeomGral()
############################################################################


############################################################################
# Reading Config files
############################################################################
# Geometry file #
#################
def ReadDom(config):

    fic = os.path.join(config, 'Computation', 'GRAL.geb')

    cfg.path = config

    if not os.path.isfile(fic):

        print("WARNING! I couldn't initialize the GRAL geometry")
        print("Please check the file:", fic)
        return

    else:

        # Read the file

        # f = open(fic, 'r')
        # data = f.readlines()
        # f.close()

        geb = []

        with open(fic, 'r') as f:
            for line in f:
                geb.append(line.split()[0])

        # data = map(lambda ln: string.split(ln, '!')[0], data)
        ind = 0

        print("GRAL domain initialized as follows:")
        print("")

        cfg.GRAL_dx = int(geb[ind])
        ind += 1
        cfg.GRAL_dy = int(geb[ind])
        ind += 2
        # cfg.GRAL_dz,
        # cfg.GRAL_ddz        = map(float, str.split(geb[ind], ','));  ind+=1
        cfg.GRAL_nx = int(geb[ind])
        ind += 1
        cfg.GRAL_ny = int(geb[ind])
        ind += 1
        cfg.GRAL_nslices = int(geb[ind])
        ind += 1
        cfg.GRAL_SG = map(int, str.split(geb[ind], ','))
        ind += 1
        cfg.GRAL_xmin = int(geb[ind])
        ind += 1
        cfg.GRAL_xmax = int(geb[ind])
        ind += 1
        cfg.GRAL_ymin = int(geb[ind])
        ind += 1
        cfg.GRAL_ymax = int(geb[ind])
        ind += 1

        print("GRAL west  side (Swiss coordinates):       ", cfg.GRAL_xmin)
        print("GRAL east  side (Swiss coordinates):       ", cfg.GRAL_xmax)
        print("GRAL south side (Swiss coordinates):       ", cfg.GRAL_ymin)
        print("GRAL north side (Swiss coordinates):       ", cfg.GRAL_ymax)
        print("number of cells in x-direction:            ", cfg.GRAL_nx)
        print("number of cells in y-direction:            ", cfg.GRAL_ny)
        # print ("Thickness of the surface layer [m]:        ", cfg.GRAL_dz0)
        # print ("Stretching factor for the vertical layers: ", cfg.GRAL_ddz)
        print("number of slices for particle counting:    ", cfg.GRAL_nslices)
        # print ("number of Source Groups:                   ", cfg.GRAL_SG)
        print("########################\n\n\n")
