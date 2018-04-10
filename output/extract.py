import numpy as np
import struct
import os


import memo2gral.globals as cfg


def conc_field(field):
    '''
    dir_conc = con file directory
    field = filename of con file (excluding the *con)

    return array contaning the concentration at each cell
    '''
    filename = os.path.join(cfg.path, 'Computation', field + '.con')
    conc = np.zeros((cfg.GRAL_nx, cfg.GRAL_ny), np.float)

    with open(filename, "rb") as f:

        # skip header
        f.read(4)

        while True:

            # read data
            data = f.read(12)

            if not data:
                break

            x, y, c = struct.unpack("iif", data)

            i = int(np.floor((x - cfg.GRAL_xmin) / cfg.GRAL_dx))
            j = int(np.floor((y - cfg.GRAL_ymin) / cfg.GRAL_dy))
            conc[i, j] = c

        np.savetxt('Concentration ' + str(field) +
                   '.txt', np.transpose(np.array(conc)))

        return np.transpose(np.array(conc))
