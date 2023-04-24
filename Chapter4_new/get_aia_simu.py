import glob
import sunpy.map
import numpy as np
from aiapy.calibrate import register, update_pointing, normalize_exposure
from calculate_DN import calculate_DN_4096
from datetime import datetime
import time

from constant import wavelength_list_aia
from gaussian_fit_aia import gaussian_fit_aia
# %%
aia_adjusted_files = sorted(glob.glob('data/AIA/*adjusted.fits'))
aia_adjusted_maps = sunpy.map.Map(aia_adjusted_files)
irradiance = np.zeros((len(aia_adjusted_maps), len(wavelength_list_aia)))
wavelength_correction = np.zeros(len(aia_adjusted_maps))
# %%


def get_aia_simu(a, b, c, d, e):

    # work out wavelength_correction
    for i in range(len(aia_adjusted_maps)):
        irradiance[i] = calculate_DN_4096(aia_adjusted_maps[i], a, b, c, d, e)
        wavelength_correction[i] = gaussian_fit_aia(wavelength_list_aia,
                                                    irradiance[i])

    # work out time_list
    time_list = []
    for aia_adjusted_map in aia_adjusted_maps:
        dt = datetime.strptime(aia_adjusted_map.meta['t_obs'],
                               '%Y-%m-%dT%H:%M:%S.%fZ')

        # Extract the day of the year from the datetime object
        day_of_year = dt.timetuple().tm_yday
        time_list.append(day_of_year)

    # Combine time_list and wavelength_correction
    aia_simu = dict(zip(time_list, wavelength_correction))

    return aia_simu

    # %%
# =============================================================================
# start = time.time()
#
# m = get_aia_simu(a=886.81, b=0.91002, c=0)
#
# end = time.time()
#
# print(end-start)
# =============================================================================
