#!/usr/bin/python
"""
Created on Thu Apr  5 10:23:40 2018

@author: mrp
"""
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import pandas as pd
import numpy as np
import os
# import matplotlib.dates as mdates
# import matplotlib.pyplot as plt

utils = importr('utils')
utils.install_packages('IDPmisc')

IDPmisc = importr('IDPmisc')


def rfbaseline(path, filename, start, end):

    baseline = pd.read_csv(os.path.join(path, filename), delimiter=';', skiprows=8,
                           header=0)
    baseline['lokal'] = pd.to_datetime(baseline['lokal'])

    pandas2ri.activate()

    baseline_rfb3 = IDPmisc.rfbaseline(
        x=baseline['lokal'], y=baseline['CH4_dry'], NoXP=100, maxit=5)

    BG = pd.DataFrame()
    BG['lokal'] = pd.Series(baseline['lokal'])
    BG['y_val'] = pd.Series(baseline_rfb3[1], index=baseline.index)
    BG['fit'] = pd.Series(baseline_rfb3[2], index=baseline.index)

    plume_BG = pd.DataFrame()
    plume_BG['lokal'] = BG['lokal'].iloc[start:end + 1]
    plume_BG['y_val'] = BG['fit'].iloc[start:end + 1]

    # fig, ax = plt.subplots(figsize=(8, 4))

    # ax.plot(baseline['lokal'], baseline['CH4_dry'], linewidth=1)
    # ax.plot(BG['lokal'], BG['fit'], color='red', linewidth=1, label='Background')
    # ax.grid(linewidth=0.5, linestyle='dotted', alpha=0.75)
    # ax.set_xlabel('Time', fontsize=14)
    # ax.set_ylabel(r'CH$_4$ [ppm]', fontsize=14)
    # ax.set_ylim([ax.set_ylim()[0], 3.2])
    # ax.set_xlim(['2018-02-10 12:25', '2018-02-10 14:45'])
    # ax.legend(fontsize=14)
    # myFmt = mdates.DateFormatter('%H:%M')
    # plt.gca().xaxis.set_major_formatter(myFmt)
    # plt.tick_params(labelsize=14)
    # plt.show()

    return np.mean(plume_BG['y_val'])
