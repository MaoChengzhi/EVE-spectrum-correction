import astropy.units as u
from astropy.constants import au, R_sun
from astropy.stats import gaussian_fwhm_to_sigma
import math


# %%
print(19.8 * (180*3600/(974.634085*math.pi))**2 / 1000)
print(4.3*180*3600/(974.634085*math.pi*1000))
