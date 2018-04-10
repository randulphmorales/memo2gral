#!usr/bin/python
"""
Created on Tue Mar 20 22:06:25 2018

@author: mrp
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('seaborn-colorblind')

path = '/Users/mrp/Desktop/Observations/Meteorology'
filename = 'Metdata_1min_TR20180210.csv'
fic = os.path.join(path, filename)

meteo = pd.read_csv(fic, delimiter=';', header=0)

meteo = meteo.set_index('datetime')
meteo.index = pd.to_datetime(meteo.index)

#=======Transforming the U and V component=====================================
alpha = np.deg2rad(60)

R01 = np.matrix([[np.cos(alpha), np.sin(alpha)],
                 [-np.sin(alpha), np.cos(alpha)]])

UV = np.zeros(len(meteo))

for i in range(len(meteo)):
    np.dot(R01, np.matrix([[meteo['U'].iloc[i]], [meteo['V'].iloc[i]]]))


meteo5 = meteo.resample('5min').mean()

#=================== PLOTTING 5 MIN AVERAGE WIND VELOCITY ======================
# fig,ax = plt.subplots(figsize = (8,4))
# ax.plot_date(meteo5.index, meteo5['Ubar'],'-',linewidth = 1.0)
# ax.plot_date(meteo.index, meteo['Ubar'],'--',linewidth = 0.3, label = None)
#
# ax.grid(linewidth = 0.5, linestyle = 'dotted', alpha = 0.75)
# ax.set_xlabel('Time', fontsize = 14)
# ax.set_ylabel(r'Velocity [ms$^{-1}$]', fontsize = 14)
# ax.set_xlim(['2018-10-02 12:25', '2018-10-02 14:45'])
#
# myFmt = mdates.DateFormatter('%H:%M')
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.tick_params(labelsize=14)
# plt.title('Wind Velocity', fontsize = 14)
#==============================================================================

#=================== PLOTTING 5 MIN AVERAGE WIND DIRECTION ====================
# fig, ax2 = plt.subplots(figsize=(8, 4))
# ax2.plot_date(meteo5.index, meteo5['Winddir'],
#               '-', color='orange', linewidth=1.0)
# ax2.plot_date(meteo.index, meteo['Winddir'], '--',
#               color='orange', linewidth=0.3, label=None)

# ax2.grid(linewidth=0.5, linestyle='dotted', alpha=0.75)
# ax2.set_xlabel('Time', fontsize=14)
# ax2.set_ylabel(r'Direction (degrees)', fontsize=14)
# ax2.set_xlim(['2018-10-02 12:25', '2018-10-02 14:45'])

# myFmt = mdates.DateFormatter('%H:%M')
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.tick_params(labelsize=14)
# plt.title('Wind Direction', fontsize=14)


# plt.show()
#==============================================================================


#=================== SAVING 5 MIN AVERAGE METDATA INTO CSV ====================
#meteo5.to_csv('Metdata_5min_TR20180210.csv', sep = ';', header = True, index = True)

#=================== METDATA INPUT FOR GRAL/GRAMM ===========================
fout = '/Users/mrp/Desktop/Observations/Output'
with open(os.path.join(fout, 'inputzr.dat'), 'w') as f:
    f.write('1\n')
    f.write('1.7\n')
    for i in range(1, len(meteo5)):
        f.write(str(i) + '\t' + str(meteo5['U*'].iloc[i]) + '\t' +
                str(meteo5['L'].iloc[i]) + '\t' +
                str(-1) + '\t' +
                str(meteo5['Vfluc'].iloc[i]) + '\t' +
                str(meteo5['UCOMP'].iloc[i]) + '\t' +
                str(meteo5['VCOMP'].iloc[i]) + '\n')
