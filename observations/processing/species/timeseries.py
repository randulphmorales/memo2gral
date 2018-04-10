#!/usr/bin/python
"""
Created on Tue Mar 20 22:46:23 2018

@author: mrp
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import os

style.use('seaborn-colorblind')

path = '/Users/mrp/Desktop/Observations/Mobile Measurements/'

LUND = pd.read_csv(os.path.join(path, 'LUND_MEMO2_TR20180210.dat'), delimiter=';', skiprows=8,
                   header=0)
RHUL = pd.read_csv(os.path.join(path, 'RHUL_MEMO2_TR20180210.dat'), delimiter=';', skiprows=8,
                   header=0)
UHEI = pd.read_csv(os.path.join(path, 'UHEI_MEMO2_TR20180210_WOAIRCORE.dat'), delimiter=';', skiprows=8,
                   header=0)
AGH = pd.read_csv(os.path.join(path, 'AGH_MEMO2_TR20180210.dat'), delimiter=';', skiprows=8,
                  header=0)

LUND['lokal'] = pd.to_datetime(LUND['lokal'])
RHUL['lokal'] = pd.to_datetime(RHUL['lokal'])
UHEI['lokal'] = pd.to_datetime(UHEI['lokal'])
AGH['lokal'] = pd.to_datetime(AGH['lokal'])

#====================== TIMESERIES PLOT OF MOKE FRACTION ======================
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot_date(RHUL['UTC'], RHUL['CH4_dry'], '-', linewidth=1.0, label='RHUL')
ax.plot_date(UHEI['UTC'], UHEI['CH4'], '-', linewidth=0.5, label='UHEI')
ax.plot_date(AGH['UTC'], AGH['CH4'], '-', linewidth=0.5, label='AGH')
ax.plot_date(LUND['UTC'], LUND['CH4'], '-', linewidth=0.5, label='LUND')

#==============================================================================
# ax.hist( RHUL['CH4_Raw'], bins = 100, label = 'RHUL',alpha = 0.3)
# ax.hist(UHEI['CH4'], bins=100, label='UHEI', alpha=0.3)
# ax.hist(AGH['CH4'], bins=100, label='AGH', alpha=0.3)
# ax.hist(LUND['CH4'], bins=100, label='LUND', alpha=0.3)
#==============================================================================

ax.grid(linewidth=0.5, linestyle='dotted', alpha=0.75)
ax.set_xlabel('Time [UTC]', fontsize=14)
ax.set_ylabel(r'CH$_4$ [ppm]', fontsize=14)
ax.set_ylim([ax.set_ylim()[0], 3.2])
ax.set_xlim(['2018-02-10 11:25', '2018-02-10 13:45'])
ax.legend(fontsize=14)
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.tick_params(labelsize=14)

plt.show()
