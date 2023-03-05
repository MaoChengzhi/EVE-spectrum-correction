import copy
import glob

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
from IPython.display import HTML

import astropy.table
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.visualization import AsymmetricPercentileInterval, ImageNormalize, LogStretch
from astropy.io import fits

import sunpy.map
import sunpy.timeseries
import sunpy.sun.constants
from sunpy.coordinates import Helioprojective


#%%
file_name='data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits'
with fits.open(file_name) as hdulist:
    hdulist.info()


#%%
astropy.io.fits.hdu.compressed.CompImageHDU?





















#%%
file_name='data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits'
aia_image=fits.getdata(file_name)

print("type: "+str(type(aia_image)))
print("shape: "+str(aia_image.shape)) 
#%%
# hdulist=fits.open()
hdulist=fits.open(file_name)
print(hdulist[0].header)
print(hdulist[1].header)

# for i in range(1000):
#     try:
#         hdulist[i]
#     except:
#         IndexError
#         break
#%%
# print(hdulist)
# plt.imshow(hdulist[0].data)
plt.imshow(hdulist[1].data, vmin=50,vmax=100)
