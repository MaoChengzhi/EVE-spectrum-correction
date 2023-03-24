import pandas as pd
import numpy as np

from astropy.stats import gaussian_fwhm_to_sigma

import sunpy.map
import sunpy.sun.constants

from scipy.io import readsav

import math

from pixel_to_world.my_pixel_to_world import my_pixel_to_world
# %%
angle_point_num_alpha = 61
offaxis_angle_x_alpha = np.linspace(-math.pi /
                                    360, math.pi/360, angle_point_num_alpha)
offaxis_angle_y_alpha = np.zeros(angle_point_num_alpha)
# %%
normalized_data = np.load("data/AIA/image_data_4096.npz")
image_data_4096 = normalized_data["image_data"]
image_data = sunpy.image.resample.resample(
    image_data_4096, dimensions=(2048, 2048))
image_shape_x, image_shape_y = image_data.shape
# %%


def wavelength_shift(Tx, Ty, A=915.53, B=0.92464):
    return A * Tx**2 + B * Ty


# %%
integral_area = []
standard_dev = 0.1*gaussian_fwhm_to_sigma
stddev = []
central_wavelength = []
for pixel_x in range(image_shape_x):
    for pixel_y in range(image_shape_y):

        # for pixel_x in range(2):
        #     for pixel_y in range(2):
        if(image_data[pixel_x][pixel_y] <= 0):
            continue
        Tx, Ty = my_pixel_to_world(2*pixel_x, 2*pixel_y)

        integral_area.append(image_data[pixel_x][pixel_y] /
                             (math.sqrt(2*math.pi)*standard_dev))
        central_wavelength.append(wavelength_shift(Tx, Ty))
        stddev.append(standard_dev)


# 使用三个2048*2048的二维数组，最后一起 flatten，放入dataframe?
# %%


# create a DataFrame from the arrays
df = pd.DataFrame({'integral_area': integral_area, 'central_wavelength': central_wavelength,
                   'stddev': stddev,
                   })

# print the DataFrame
print(df)
# %%
df_combined = pd.concat(df)
# %%
df.to_csv('pixel_df.csv')
