# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:59:00 2018

@author: mrp
"""
import numpy as np
import os


def obs_data(path, filename, start, end, dir=1):
    fic = os.path.join(path, filename)

    lon, lat, ppm = np.genfromtxt(fic, delimiter=';',
                                  skip_header=start - 1,
                                  max_rows=end - start + 1,
                                  usecols=(2, 3, 4),
                                  unpack=True)

    P1 = (166.3 + 4.1, 52.1 + 2.669)
    P2 = (5.589 + 4.1, 52.1 + 135.4)

    x0, y0 = P1[0], P1[1]
    x1, y1 = P2[0], P2[1]
    scale_dist = np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    if dir == 1:
        lon = np.concatenate([[4.693709], lon, [4.691322]])
        lat = np.concatenate([[52.727044], lat, [52.728238]])
        ppm = np.concatenate([[1.96], ppm, [1.96]])

    elif dir == 2:
        lon = np.concatenate([[4.691322], lon, [4.693709]])
        lat = np.concatenate([[52.728238], lat, [52.727044]])
        ppm = np.concatenate([[1.96], ppm, [1.96]])

    dist = np.sqrt((lon[0] - lon[-1]) ** 2 + (lat[0] - lat[-1]) ** 2)

    def dis(lon, lat):
        rel_dis = np.zeros(len(lon), np.float)

        for i in range(len(lon)):
            rel_dis[i] = (np.sqrt((lon[i] - lon[0]) ** 2 +
                                  (lat[i] - lat[0]) ** 2) / dist) * scale_dist

        return rel_dis

    obs_dis = dis(lon, lat)
    obs_array = np.array([obs_dis[1:-1], ppm[1:-1]])

    return obs_array


def obs_dataT2(path, filename, start, end, dir=1):

    fic = os.path.join(path, filename)

    lon, lat, ppm = np.genfromtxt(fic, delimiter=';',
                                  skip_header=start - 1,
                                  max_rows=end - start + 1,
                                  usecols=(2, 3, 4),
                                  unpack=True)

    P1 = (166.3 + 4.1, 52.1 + 2.669)
    P2 = (5.589 + 4.1, 52.1 + 135.4)

    x0, y0 = P1[0], P1[1]
    x1, y1 = P2[0], P2[1]
    scale_dist = np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    if dir == 1:
        lon = np.concatenate([[4.695747], lon, [4.693276]])
        lat = np.concatenate([[52.727632], lat, [52.729874]])
        ppm = np.concatenate([[1.96], ppm, [1.96]])

    elif dir == 2:
        lon = np.concatenate([[4.693276], lon, [4.695747]])
        lat = np.concatenate([[52.729874], lat, [52.727632]])
        ppm = np.concatenate([[1.96], ppm, [1.96]])

    dist = np.sqrt((lon[0] - lon[-1]) ** 2 + (lat[0] - lat[-1]) ** 2)

    def dis(lon, lat):
        rel_dis = np.zeros(len(lon), np.float)

        for i in range(len(lon)):
            rel_dis[i] = (np.sqrt((lon[i] - lon[0])**2 +
                                  (lat[i] - lat[0])**2) / dist) * scale_dist

        return rel_dis

    obs_dis = dis(lon, lat)
    obs_array = np.array([obs_dis[1:-1], ppm[1:-1]])
    return obs_array
