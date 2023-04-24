import sunpy.map
import glob
import numpy as np
from astropy.stats import gaussian_fwhm_to_sigma
from pixel_to_world.my_pixel_to_world import my_pixel_to_world
from constant import wavelength_list_aia

from math import pi
from math import sqrt
# %%


def calculate_DN_4096(aia_adjusted_map, a=8e2, b=0, c=0.9, d=0, e=-1e-2):
    '''


    Parameters
    ----------
    aia_adjusted_map : TYPE
        DESCRIPTION.

    Returns
    the DN at different wavelength
    -------
    None.

    '''

    image_data = aia_adjusted_map.data
    image_shape_x, image_shape_y = image_data.shape
    r_sun = aia_adjusted_map.meta['rsun_obs']*pi/(3600*180)

    total_irradiance = 0
    stddev = np.zeros((image_shape_x, image_shape_y))+0.1 * \
        gaussian_fwhm_to_sigma  # unit: nm

    # Create NumPy arrays for pixel indices and image data
    pixel_x = np.arange(image_shape_x)
    pixel_y = np.arange(image_shape_y)
    Px, Py = np.meshgrid(pixel_x, pixel_y, indexing='ij')

    # Compute Tx and Ty for all pixels in parallel
    Tx, Ty = my_pixel_to_world(Px, Py)  # 使用4096的照片

    # only use pixels with value>0
    image_data = image_data*(image_data > 0)

    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image_data / (np.sqrt(2 * pi) * stddev)
    mean = wavelength_shift(Tx, Ty, a, b, c, d, e)
    coeff = np.array([amplitude, mean, stddev])

    # Compute total_irradiance using vectorized NumPy operations
    total_irradiance = np.sum(my_Gaussian1D(
        wavelength_list_aia, *coeff), axis=(1, 2))  # size:(12,4096,4096)

    return total_irradiance

# %%


def wavelength_shift(Tx, Ty, a, b, c, d, e):
    '''


    Parameters
    ----------
    Tx : 

    Ty : 

    A : 
    B : 

    Returns
    -------
        Wavelength shift at a given angle.

    '''

    return a * Tx**2 + b * Tx + c*Ty**2 + d * Ty+e


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


# %%
