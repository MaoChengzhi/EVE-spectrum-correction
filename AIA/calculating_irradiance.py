import copy
import glob

import numpy as np

from IPython.display import HTML

import astropy.table
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.io import fits
from astropy.modeling.models import Gaussian1D
from astropy.modeling import fitting,models
from astropy.stats import gaussian_fwhm_to_sigma

import sunpy.map
import sunpy.sun.constants
from sunpy.coordinates import Helioprojective
from sunpy.map.maputils import all_coordinates_from_map, coordinate_is_on_solar_disk
from sunpy.coordinates import frames

import math

import time

from scipy import optimize

from my_pixel_to_world import my_pixel_to_world
#%%
AIA_filename="data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits"
m_aia=sunpy.map.Map(AIA_filename)
image_data=m_aia.data
image_shape_x,image_shape_y=m_aia.data.shape
#%%

#%%
def wavelength_shift(Tx,Ty):
    return  909.1 * Tx**2 + 0.921*Ty
def my_Gaussian1D(x,amplitude=1, mean=0, stddev=1):
    return amplitude*math.e**(-(x-mean)**2/(2*stddev**2))

def calculating_irradiance(wavelength,offaxis_angle_x,offaxis_angle_y):
    total_irradiance=0
    # for pixel_x in range(image_shape_x):
    #     for pixel_y in range(image_shape_y): #first only calculate a small fraction to check 
    for pixel_x in np.linspace(0,image_shape_x-1,200,dtype=int):
        for pixel_y in np.linspace(0,image_shape_y-1,200,dtype=int):
            Tx,Ty=my_pixel_to_world(pixel_x,pixel_y)

            Tx+=offaxis_angle_x
            Ty+=offaxis_angle_y
            
            stddev=0.1*gaussian_fwhm_to_sigma
            amplitude=image_data[pixel_x][pixel_y]/(math.sqrt(2*math.pi)*stddev)
            coeff=(amplitude,  #amplitude
                   wavelength_shift(Tx,Ty),      #mean
                   stddev)    #stddev

            total_irradiance+=my_Gaussian1D(wavelength,*coeff)
    return total_irradiance