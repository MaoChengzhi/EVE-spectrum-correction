import numpy as np

from astropy.stats import gaussian_fwhm_to_sigma

import sunpy.map
import sunpy.sun.constants

import math

from my_pixel_to_world import my_pixel_to_world

# %% Initialize
wavelength_point_num = 15
wavelength_list = np.linspace(-0.1, 0.15, wavelength_point_num)

# Cruciformscan in alpha direction
angle_point_num_alpha = 61
DN_alpha = np.zeros((angle_point_num_alpha, wavelength_point_num))
offaxis_angle_x_alpha = np.linspace(-math.pi /
                                    360, math.pi/360, angle_point_num_alpha)
offaxis_angle_y_alpha = np.zeros(angle_point_num_alpha)

# Cruciformscan in beta direction
angle_point_num_beta = 61
DN_beta = np.zeros((angle_point_num_beta, wavelength_point_num))
offaxis_angle_x_beta = np.zeros(angle_point_num_beta)
offaxis_angle_y_beta = np.linspace(-math.pi /
                                   360, math.pi/360, angle_point_num_beta)

# %%


def calculate_DN_alpha(A, i):
    '''
    DN in wavelength list in angle_point_num_alpha. For parallel processing

    Returns
    -------
    ndarray
        DN_alpha 

    '''
    return calculating_DN(wavelength_list,
                          offaxis_angle_x_alpha[i],
                          offaxis_angle_y_alpha[i], A)


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


# %%

AIA_filename = "data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits"
m_aia = sunpy.map.Map(AIA_filename)
image_data = m_aia.data
image_shape_x, image_shape_y = m_aia.data.shape

# %%


def wavelength_shift(Tx, Ty, A=909.2, B=0.9214):
    '''


    Parameters
    ----------
    Tx : 

    Ty : 

    A : TYPE, optional
        DESCRIPTION. The default is 909.2.
    B : TYPE, optional
        DESCRIPTION. The default is 0.9214.

        The orginal coeff are 19.8 and 4.3, but Tx,Ty here are in radian.

        The unit conversion process is in "unit_conversion.py"

    Returns
    -------
        Wavelength shift at a given angle.


    '''
    return A * Tx**2 + B*Ty


def my_Gaussian1D(x, amplitude, mean, stddev):
    '''
    I use this function written myself, because Gaussian1D in astropy is too slow.

    Returns
    -------
    Value of the 1D Gaussian curve at a given point
    '''
    return amplitude*math.e**(-(x-mean)**2/(2*stddev**2))


def calculating_DN(wavelength, offaxis_angle_x, offaxis_angle_y, A):
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
    stddev = 0.1*gaussian_fwhm_to_sigma
# =============================================================================
#     Only calculate a small fraction to check
#     for pixel_x in np.linspace(0,image_shape_x-1,200,dtype=int):
#         for pixel_y in np.linspace(0,image_shape_y-1,200,dtype=int):
# =============================================================================
    for pixel_x in range(image_shape_x):
        for pixel_y in range(image_shape_y):
            if image_data[pixel_x][pixel_y] <= 0:
                continue

            Tx, Ty = my_pixel_to_world(pixel_x, pixel_y)
            Tx += offaxis_angle_x
            Ty += offaxis_angle_y

            amplitude = image_data[pixel_x][pixel_y] / \
                (math.sqrt(2*math.pi)*stddev)
            coeff = (amplitude,  # amplitude
                     wavelength_shift(Tx, Ty, A),  # mean
                     stddev)  # stddev

            total_irradiance += my_Gaussian1D(wavelength, *coeff)
    return total_irradiance

# run for 48847s 13h on Feb 2
