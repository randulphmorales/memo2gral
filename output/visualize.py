import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os

import memo2gral.globals as cfg


def vis_field(conc_field):
    '''
    dir_conc = directory of the GRAL project

    dom = dictionary containing xmin, xmax, dx, ymin, ymax, ymin, dy

    conc_field = array containing the concentration at each cell
    '''
    lon = np.arange(cfg.GRAL_xmin, cfg.GRAL_xmax, cfg.GRAL_dx)
    lat = np.arange(cfg.GRAL_ymin, cfg.GRAL_ymax, cfg.GRAL_dy)

    levels = np.linspace(0.0001, np.amax(conc_field), 100)
    cmap = cm.GnBu

    fig, ax = plt.subplots(figsize=(8, 6))

    im = ax.contourf(lon, lat, conc_field,
                     cmap=cmap,
                     levels=levels,
                     vmin=0,
                     vmax=np.amax(conc_field),
                     alpha=0.50)
    ax.plot(4.1, 52.1, 'ro')

    imap = ax.imshow(mpimg.imread(os.path.join(cfg.path, 'Maps', 'tr20180210.jpg')),
                     alpha=0.7,
                     extent=[cfg.GRAL_xmin, cfg.GRAL_xmax,
                             cfg.GRAL_ymin, cfg.GRAL_ymax],
                     shape=(len(lon), len(lat)))

    ax.grid(linewidth=0.5, linestyle='dotted', alpha=0.75)
    plt.title(r'$CH_4$ Dispersion')

    ##############################################################
    # Colorbar customization
    #############################################################
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.10)
    cbar = plt.colorbar(im, cax=cax)
    cbar.ax.set_ylabel(r'$\mu g / m^3$')

    plt.tight_layout()
    plt.show()
    fig.savefig('Concentration Field.png')

    return ax
