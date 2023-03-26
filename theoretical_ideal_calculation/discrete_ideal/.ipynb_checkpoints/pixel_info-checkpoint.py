import pandas as pd
import numpy as np

from astropy.stats import gaussian_fwhm_to_sigma

import sunpy.map
import sunpy.sun.constants

from scipy.io import readsav

import math

from pixel_to_world.my_pixel_to_world import my_pixel_to_world
# %%

normalized_data = np.load("data/AIA/image_data_4096.npz")
image_data_4096 = normalized_data["image_data"]
image_data = sunpy.image.resample.resample(
    image_data_4096, dimensions=(2048, 2048))
image_shape_x, image_shape_y = image_data.shape
# %%


def wavelength_shift(Tx, Ty, A=915.53, B=0.92464):
    '''
    Parameters
    ----------
    Tx : 

    Ty : 

    A : TYPE, optional
        DESCRIPTION. The default is 915.53.
    B : TYPE, optional
        DESCRIPTION. The default is 0.92464.

        The orginal coeff are 19.8 and 4.3, but Tx,Ty here are in radian.

        The unit conversion process is in "unit_conversion.py"

    Returns
    -------
        Wavelength shift at a given angle.


    '''

    return A * Tx**2 + B * Ty


# %%

# %%
amplitude = []
standard_dev = 0.1*gaussian_fwhm_to_sigma
stddev = []
central_wavelength = []


for pixel_x in range(image_shape_x):
    for pixel_y in range(image_shape_y):
        
# for pixel_x in range(2):
#     for pixel_y in range(2):
        Tx, Ty = my_pixel_to_world(2*pixel_x, 2*pixel_y)
        
        stddev.append(standard_dev)
        amplitude.append(image_data[pixel_x][pixel_y] /
                         (math.sqrt(2*math.pi)*standard_dev))
        
        central_wavelength.append(wavelength_shift(Tx, Ty))
# %%



# create a DataFrame from the arrays
df = pd.DataFrame({'amplitude': amplitude, 'stddev': stddev, 'central_wavelength': central_wavelength})

# print the DataFrame
print(df)
#%%
df.to_csv('pixel_df.csv')
