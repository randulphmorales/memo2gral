#!usr/bin/python
import numpy as np
import pandas as pd
import os

filename = 'RHUL_MEMO2_TR20180210'
filename2 = 'UHEI_MEMO2_TR'
filename3 = 'AGH_MEMO2_TR20180210_ND'
filename4 = 'AGH_MEMO2_TR20180210'
filename5 = 'UU_MEMO2_TR20180210'
filename6 = 'Utrect_MEMO2_TR20180210'


def write_kml(filename):
    fic = os.path.join(filename + '.dat')

    lon, lat, CH4_conc = np.loadtxt(
        fic, skiprows=9, usecols=(2, 3, 4), delimiter=';', unpack=True)
    datetime = pd.read_csv(fic, delimiter=';', usecols=[
                           1], skiprows=9, header=None)
    datetime[1] = pd.to_datetime(datetime[1])

    with open(str(filename) + '.kml', 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        f.write('\t<Document>\n')
        f.write('\t\t<name>' + str(filename) + '</name>\n')
        f.write('\t\t<Style id="yellowLineGreenPoly">\n')
        f.write('\t\t\t<LineStyle>\n')
        f.write('\t\t\t\t<color>7f00ffff</color>\n')
        f.write('\t\t\t\t<width>4</width>\n')
        f.write('\t\t\t</LineStyle>\n')
        f.write('\t\t\t<Polystyle>\n')
        f.write('\t\t\t\t<color>7f00ff00</color>\n')
        f.write('\t\t\t</Polystyle>\n')
        f.write('\t\t</Style>\n')

        for i in range(2300, 5100, 100):
            f.write('\t\t<Placemark>\n')
            f.write(
                '\t\t\t<name>' + str(datetime.iloc[i]) + '_' + str(datetime.iloc[i + 100]) + '</name>\n')
            f.write('\t\t\t<styleUrl>#yellowLineGreenPoly</styleUrl>\n')
            f.write('\t\t\t<LineString>\n')
            f.write('\t\t\t\t<extrude>1</extrude>\n')
            f.write('\t\t\t\t<tessellate>1</tessellate>\n')
            f.write('\t\t\t\t<altitudeMode>absolute</altitudeMode>\n')
            f.write('\t\t\t\t<coordinates>\n')

            for i in range(i, i + 101):
                f.write('\t\t\t\t' + str(lon[i]) + ',' + str(lat[i]
                                                             ) + ',' + str(CH4_conc[i] * 100 - 195) + '\n')

            f.write('\t\t\t\t</coordinates>\n')
            f.write('\t\t\t</LineString>\n')
            f.write('\t\t</Placemark>\n')
        f.write('\t</Document>\n')
        f.write('</kml>\n')
    return


write_kml(filename)
