import astropy.units as u
from astropy.constants import au, R_sun
from astropy.stats import gaussian_fwhm_to_sigma
import math
import numpy as np
# %%
# R_sun = 7 e8   m
# au =￼￼￼  1.5 e11 m
print(19.8 * (au/R_sun)**2 * (math.pi/(180*60))**2)
# 0.0774
print(4.3 * (au/R_sun)*(math.pi/(180*60)))
# 0.270
# %%
print(19.8*(au/R_sun)**2 / 1000)
print(4.3*(au/R_sun)/1000)

# %%
l = [1, '2']
np.savez("test.npz", l=l)
# %%
a = np.load("test.npz")
