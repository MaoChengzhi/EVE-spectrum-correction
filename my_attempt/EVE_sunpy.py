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
from astropy.modeling.models import Gaussian1D
from astropy.modeling import fitting

import sunpy.map
import sunpy.timeseries as ts
import sunpy.sun.constants
from sunpy.coordinates import Helioprojective
import sunpy

import asdf
#%%
EVL_filename="data\EVE\EVL_L2_2011027_16_007_02.fit.gz"
EVS_filename="data\EVE\EVS_L2_2011027_16_007_02.fit.gz"
hdulist_EVS=fits.open(EVS_filename,output_verify='exception',mode='readonly')
#%%
EVS=sunpy.io.read_file(EVS_filename)
EVL=sunpy.io.read_file(EVL_filename)
#%%
type(EVS)
EVS[1].data
#%%
EVS_asdf=asdf.open(EVS_filename)
