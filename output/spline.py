import numpy as np
from scipy.interpolate import interp1d


def modinterp(model, obs, bg):

    obsi = []
    obsj = []
    modelj = []

    for i in range(len(obs[0])):
        if (obs[1][i] - bg >= 0) and ((abs(obs[1][i] - bg) >= 1e-3)):
            obsi = np.append(obsi, obs[0][i])
            obsj = np.append(obsj, obs[1][i] - bg)

    ##### INTERPOLATING FUNCTION #####
    minterp1d = interp1d(model[0], model[1])

    for i in range(len(obsi)):
        modelj = np.append(modelj, minterp1d(obsi[i]))

    qqplot = np.array([modelj, obsj])

    return qqplot


def obsinterp(obs, bg):
    obsi = []
    obsj = []

    for i in range(len(obs[0])):
        if (obs[1][i] - bg >= 0) and ((abs(obs[1][i] - bg) >= 1e-3)):
            obsi = np.append(obsi, obs[0][i])
            obsj = np.append(obsj, obs[1][i] - bg)

    obsij = np.array([obsi, obsj])

    ### INTERPOLATING FUNCTION ####
    ointerp1d = interp1d(obsij[0], obsij[1])

    obsintij = np.zeros((100, 100), np.float)
    obsintij[0] = np.linspace(obsij[0][0], obsij[0][-1], 100)

    for i in range(len(obsintij[0])):
        obsintij[1][i] = ointerp1d(obsintij[0][i])

    return obsintij
