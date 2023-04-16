import numpy as np

from astropy.stats import gaussian_fwhm_to_sigma

import sunpy.map
import sunpy.sun.constants

from scipy.io import readsav

import math
from math import pi
from math import sqrt

from pixel_to_world.my_pixel_to_world import my_pixel_to_world

# %% Initialize
wavelength_point_num = 36
wavelength_list = np.linspace(-0.1, 0.25, wavelength_point_num)
# P43 图3.3 横坐标波长范围  单位nm

# Cruciformscan in alpha direction
# P42 步骤四   采用弧度制
angle_point_num_alpha = 61
offaxis_angle_x_alpha = np.linspace(-math.pi /
                                    360, math.pi/360, angle_point_num_alpha)
offaxis_angle_y_alpha = np.zeros(angle_point_num_alpha)


# Cruciformscan in beta direction
# P42 步骤四   采用弧度制
angle_point_num_beta = 61
offaxis_angle_x_beta = np.zeros(angle_point_num_beta)
offaxis_angle_y_beta = np.linspace(-math.pi /
                                   360, math.pi/360, angle_point_num_beta)

# %%


def calculate_DN_alpha(i):
    '''
    DN in wavelength list in angle_point_num_alpha. For parallel processing

    Returns
    -------
    ndarray
        DN_alpha 

    '''
    return calculating_DN(wavelength_list,
                          offaxis_angle_x_alpha[i], offaxis_angle_y_alpha[i])


def calculate_DN_beta(j):
    '''
    DN in wavelength list in angle_point_num_beta. For parallel processing

    Returns
    -------
    ndarray
        DN_beta 

    '''
    return calculating_DN(wavelength_list,
                          offaxis_angle_x_beta[j], offaxis_angle_y_beta[j])


# %% 2048

normalized_data = np.load("data/AIA/image_data_4096_normalized.npz")
image_data_4096 = normalized_data["image_data"]
image_data = sunpy.image.resample.resample(
    image_data_4096, dimensions=(2048, 2048))
image_shape_x, image_shape_y = image_data.shape

# sav_filename = "data_IDL/IDL_data.sav"
# sav_data = readsav(sav_filename)
# image_data_4096 = sav_data['out_data']
# image_data = sunpy.image.resample.resample(
#     image_data_4096, dimensions=(2048, 2048))
# image_shape_x, image_shape_y = image_data.shape
# %%


def wavelength_shift(Tx, Ty, A=886.81, B=0.91002):
    '''


    Parameters
    ----------
    Tx : 

    Ty : 

    A : TYPE, optional
        DESCRIPTION. The default is 886.81.
    B : TYPE, optional
        DESCRIPTION. The default is 0.91002.

        The orginal coeff are 19.8 and 4.3, but Tx,Ty here are in radian.

        The unit conversion process is in "unit_conversion.py"

    Returns
    -------
        Wavelength shift at a given angle.


    '''

    return A * Tx**2 + B * Ty


def my_Gaussian1D(wavelength_list, amplitude, mean, stddev):
    '''
    I use this function written myself, because Gaussian1D in astropy is too slow.

    Returns
    -------
    Value of the 1D Gaussian curve at a given point
    '''

    #     x shape: (25,)
    # amplitude, mean, stddev shape:(2048,2048)

    # Use a list comprehension to calculate the Gaussian curve for each wavelength
    results = np.array([amplitude * np.exp(-(x - mean) ** 2 / (2 * stddev ** 2))
                        for x in wavelength_list])

    return results


def calculating_DN(wavelength_list, offaxis_angle_x, offaxis_angle_y):
    '''
    Add up each the DN of each pixel 

    Parameters
    ----------
    wavelength : a number near 30.38 (nm)

    offaxis_angle_x : offaxis alpha angle of center of the image/Sun

    offaxis_angle_y : offaxis beta angle of center of the image/Sun

    Returns
    -------
    DN(digital number): at a given offaxis angle and a give wavelength

    '''

    total_irradiance = 0
    stddev = np.zeros((image_shape_x, image_shape_y))+0.1 * \
        gaussian_fwhm_to_sigma  # unit: nm

    # Create NumPy arrays for pixel indices and image data
    pixel_x = np.arange(image_shape_x)
    pixel_y = np.arange(image_shape_y)
    Px, Py = np.meshgrid(pixel_x, pixel_y, indexing='ij')

    # Compute Tx and Ty for all pixels in parallel
    Tx, Ty = my_pixel_to_world(2 * Px, 2 * Py)  # 使用2048的照片，所以乘以2
    Tx += offaxis_angle_x  # P42 步骤三 四 将卫星整体偏转
    Ty += offaxis_angle_y  # P42 步骤三 四 将卫星整体偏转

    # Select pixels on the solar disk
    disk = (Tx-offaxis_angle_x)**2+(Ty-offaxis_angle_y)**2 -\
        (974.634085*math.pi/(3600*180))**2 < 0  # according to 'rsun_obs'
    image_data_disk = image_data*disk

    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image_data_disk / (np.sqrt(2 * pi) * stddev)
    mean = wavelength_shift(Tx, Ty)
    coeff = np.array([amplitude, mean, stddev])

    # Compute total_irradiance using vectorized NumPy operations
    total_irradiance = np.sum(my_Gaussian1D(
        wavelength_list, *coeff), axis=(1, 2))  # P42 步骤二

    return total_irradiance


# =============================================================================
# previous method : without vectorizing
#     total_irradiance = 0
#     stddev = 0.1*gaussian_fwhm_to_sigma  # unit: nm
#     for pixel_x in range(image_shape_x):
#         for pixel_y in range(image_shape_y):
#             if image_data[pixel_x][pixel_y] <= 0:
#                 continue
#
#             Tx, Ty = my_pixel_to_world(2*pixel_x, 2*pixel_y)  # 使用2048的照片，所以乘以2
#             Tx += offaxis_angle_x  # P42 步骤三 四 将卫星整体偏转
#             Ty += offaxis_angle_y  # P42 步骤三 四 将卫星整体偏转
#
#             amplitude = image_data[pixel_x][pixel_y] / \
#                 (math.sqrt(2*math.pi)*stddev)
#             coeff = (amplitude,  # amplitude
#                      wavelength_shift(Tx, Ty),  # mean
#                      stddev)  # stddev
#
#             total_irradiance += my_Gaussian1D(wavelength, *coeff)  # P42 步骤二
#     return total_irradiance
# =============================================================================

# run for 48847s 13h on Feb 2
# %%

# %%
# a = calculating_DN(np.linspace(-0.1, 0.2, 30), 0, 0)
# a.shape
