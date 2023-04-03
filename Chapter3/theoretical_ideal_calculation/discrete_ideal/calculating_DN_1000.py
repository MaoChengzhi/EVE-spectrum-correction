import numpy as np

from astropy.stats import gaussian_fwhm_to_sigma

import sunpy.map
import sunpy.sun.constants

from scipy.io import readsav

import math

import matplotlib.pyplot as plt

# %% Initialize
wavelength_point_num = 20
wavelength_list = np.linspace(-1, 2, wavelength_point_num)
# P43 图3.3 横坐标波长范围  单位nm

# Cruciformscan in alpha direction
# P42 步骤四   采用弧度制
angle_point_num_alpha = 10
DN_alpha = np.zeros((angle_point_num_alpha, wavelength_point_num))
offaxis_angle_x_alpha = np.linspace(-500, 500, angle_point_num_alpha)
offaxis_angle_y_alpha = np.zeros(angle_point_num_alpha)

# Cruciformscan in beta direction
# P42 步骤四   采用弧度制
angle_point_num_beta = 10
DN_beta = np.zeros((angle_point_num_beta, wavelength_point_num))
offaxis_angle_y_beta = np.linspace(-500, 500, angle_point_num_alpha)
offaxis_angle_x_beta = np.zeros(angle_point_num_beta)

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

image_data = np.zeros((1000, 1000))
image_shape_x, image_shape_y = image_data.shape
for i in range(image_shape_x):
    for j in range(image_shape_y):
        if((i-500)**2+(j-500)**2 < 500**2):
            image_data[i][j] = 1


# %%
def my_pixel_to_world(pixel_x, pixel_y):
    return pixel_x-500, pixel_y-500


def wavelength_shift(T_x, T_y):
    '''


    Parameters
    ----------


    Returns
    -------
        Wavelength shift at a given angle.


    '''

    return T_x**2/1000000


def my_Gaussian1D(x, amplitude, mean, stddev):
    '''
    I use this function written myself, because Gaussian1D in astropy is too slow.

    Returns
    -------
    Value of the 1D Gaussian curve at a given point
    '''
    return amplitude*math.e**(-(x-mean)**2/(2*stddev**2))


def calculating_DN(wavelength, offaxis_angle_x, offaxis_angle_y):
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
    stddev = 0.5
# =============================================================================
#     Only calculate a small fraction to check
#     for pixel_x in np.linspace(0,image_shape_x-1,200,dtype=int):
#         for pixel_y in np.linspace(0,image_shape_y-1,200,dtype=int):
# =============================================================================
    for pixel_x in range(image_shape_x):
        for pixel_y in range(image_shape_y):
            if image_data[pixel_x][pixel_y] <= 0:
                continue

            Tx, Ty = my_pixel_to_world(pixel_x, pixel_y)  # 使用2048的照片，所以乘以2
            Tx += offaxis_angle_x  # P42 步骤三 四 将卫星整体偏转
            Ty += offaxis_angle_y  # P42 步骤三 四 将卫星整体偏转

            amplitude = image_data[pixel_x][pixel_y] / \
                (math.sqrt(2*math.pi)*stddev)
            coeff = (amplitude,  # amplitude
                     wavelength_shift(Tx, Ty),  # mean
                     stddev)  # stddev

            total_irradiance += my_Gaussian1D(wavelength, *coeff)  # P42 步骤二
    return total_irradiance
