from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os

import memo2gral.globals as cfg


def interp2d(P1, P2, conc_field, show=1):
  x0, y0 = P1[0], P1[1]
  x1, y1 = P2[0], P2[1]

  lon = np.arange(cfg.GRAL_xmin, cfg.GRAL_xmax, cfg.GRAL_dx)
  lat = np.arange(cfg.GRAL_ymin, cfg.GRAL_ymax, cfg.GRAL_dy)
  interp_field = interpolate.interp2d(lon, lat, conc_field)

  interp_lon = np.linspace(x0, x1, 100)
  interp_lat = np.linspace(y0, y1, 100)

  dist = np.sqrt((x0 - x1)**2 + (y0 - y1)**2)

  i_array = np.linspace(0, dist, 100)
  j_array = np.zeros(100, np.float)

  interp_conc = np.zeros((100, 100), np.float)

  for j in range(len(j_array)):
    j_array[j] = interp_field(interp_lon[j], interp_lat[j])

  if show == 1:

    interp_conc = [i_array, j_array]

    levels = np.linspace(0.0001, np.amax(conc_field), 100)
    cmap = cm.GnBu

    fig, ax = plt.subplots(figsize=(8, 6))

    im = ax.contourf(lon, lat, conc_field,
                     cmap=cmap,
                     levels=levels,
                     vmin=0,
                     vmax=np.amax(conc_field),
                     alpha=0.50)

    ax.imshow(mpimg.imread(os.path.join(cfg.path, 'Maps', 'tr20180210.jpg')),
              alpha=0.7,
              extent=[cfg.GRAL_xmin, cfg.GRAL_xmax,
                      cfg.GRAL_ymin, cfg.GRAL_ymax],
              shape=(len(lon), len(lat)))

    ax.plot(4.1, 52.1, 'ro')
    ax.plot([x0, x1], [y0, y1], '-')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.10)
    cbar = plt.colorbar(im, cax=cax)
    cbar.ax.set_ylabel(r'ppm')

    plt.tight_layout()
    plt.show()

  elif show == 2:

    interp_conc = [i_array, j_array]

  return interp_conc
