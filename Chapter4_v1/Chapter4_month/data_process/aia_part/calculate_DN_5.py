
from astropy.stats import gaussian_fwhm_to_sigma
from .pixel_to_world.my_pixel_to_world import my_pixel_to_world
from .data.constant import wavelength_list_aia
import cupy as cp

from math import pi
# %%


def calculate_DN_5(aia_adjusted_map, a, b,c, d,  e):
    '''
    a * Tx**2 + b * Tx + c*Ty**2 + d * Ty+e

    Parameters
    ----------
    aia_adjusted_map : TYPE
        DESCRIPTION.

    Returns
    the DN at different wavelength
    -------
    None.

    '''

    image_data = cp.array(aia_adjusted_map.data)
    image_shape_x, image_shape_y = image_data.shape

    total_irradiance = 0
    stddev = cp.zeros((image_shape_x, image_shape_y))+0.1 * \
        gaussian_fwhm_to_sigma  # unit: nm

    # Create NumPy arrays for pixel indices and image data
    pixel_x = cp.arange(image_shape_x)
    pixel_y = cp.arange(image_shape_y)
    Px, Py = cp.meshgrid(pixel_x, pixel_y, indexing='ij')

    # Compute Tx and Ty for all pixels in parallel
    Tx, Ty = my_pixel_to_world(Px, Py)  # 使用4096的照片

    # only use pixels with value>0
    image_data = image_data*(image_data > 0)

    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image_data / (cp.sqrt(2 * pi) * stddev)
    mean = wavelength_shift_5(Tx, Ty, a,b,c, d, e)
    coeff = cp.array([amplitude, mean, stddev])

    # Compute total_irradiance using vectorized NumPy operations
    total_irradiance = cp.sum(my_Gaussian1D(
        wavelength_list_aia, *coeff), axis=(1, 2))  # size:(12,4096,4096)

    return total_irradiance

# %%


def wavelength_shift_5(Tx, Ty, a,b,c, d, e):
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

    return a * Tx**2 + b * Tx+c*Ty**2+d * Ty+e


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
    results = cp.array([amplitude * cp.exp(-(x - mean) ** 2 / (2 * stddev ** 2))
                        for x in wavelength_list])

    return results


