import astropy.units as u
from astropy.constants import au, R_sun
from astropy.stats import gaussian_fwhm_to_sigma
import math
import numpy as np
from astropy.constants import au, R_sun

# %%
transunit = ((au/R_sun).value)**2 / 1000
# %%  P38 3.2  本应的系数
# R_sun = 7 e8   m
# au =￼￼￼  1.5 e11 m
print(19.7 * transunit)
# 0.0774
print(4.3 * (au/R_sun)*(math.pi/(180*60)))
# 0.270

# %% P38 3.2  有问题的系数(?)化为我的弧度制度

print(0.0752 * ((180*60)/math.pi)**2 / 1000)
# 0.0774
print(0.265 * ((180*60)/math.pi)**2 / 1000)

# %% 我用的
print(19.8*(au/R_sun)**2 / 1000)
print(4.3*(au/R_sun)/1000)

# %%
l = [1, '2']
np.savez("test.npz", l=l)
# %%
a = np.load("test.npz")
