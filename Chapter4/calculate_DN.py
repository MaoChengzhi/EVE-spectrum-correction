import sunpy.map
import glob
import numpy as np
from astropy.stats import gaussian_fwhm_to_sigma
from pixel_to_world.my_pixel_to_world import my_pixel_to_world
from constant import wavelength_list_aia

from math import pi
from math import sqrt
# %%


def calculate_DN_4096(aia_adjusted_map, a=886.81, b=0.91002, c=0):
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

    '''
    Add up each the DN of each pixel 

    Parameters
    ----------
    wavelength : a number near 30.38 (nm)


    Returns
    -------
    DN(digital number): at a given offaxis angle and a give wavelength

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

    # Select pixels on the solar disk
    disk = Tx**2+Ty**2 - r_sun**2 < 0  # according to 'rsun_obs'
    image_data_disk = image_data*disk

    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image_data_disk / (np.sqrt(2 * pi) * stddev)
    mean = wavelength_shift(Tx, Ty, a, b, c)
    coeff = np.array([amplitude, mean, stddev])

    # Compute total_irradiance using vectorized NumPy operations
    total_irradiance = np.sum(my_Gaussian1D(
        wavelength_list_aia, *coeff), axis=(1, 2))  # size:(12,4096,4096)

    return total_irradiance

# %%


def wavelength_shift(Tx, Ty, a, b, c):
    '''


    Parameters
    ----------
    Tx : 

    Ty : 

    A : TYPE, optional
        DESCRIPTION. The default is .  19.8 ~ 886.81
        程学长的 18.66 就是 835.7
    B : TYPE, optional
        DESCRIPTION. The default is ?.   4.3 ~ 0.91002

        The orginal coeff are 19.8 and 4.3, but Tx,Ty here are in radian.

        The unit conversion process is in "unit_conversion.py"

    Returns
    -------
        Wavelength shift at a given angle.

    '''

    return a * Tx**2 + b * Ty + c


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

# aia_adjusted_files = sorted(glob.glob('data/AIA/*adjusted.fits'))
# aia_adjusted_maps = sunpy.map.Map(aia_adjusted_files)
# # %%

# a = calculate_DN_4096(aia_adjusted_maps[0])
