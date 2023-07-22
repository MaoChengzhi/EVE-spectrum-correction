import numpy as np
import cupy as cp

from astropy.stats import gaussian_fwhm_to_sigma
import sunpy.map
import sunpy.sun.constants
from scipy.io import readsav



# %% Initialize
wavelength_point_num = 25
wavelength_list = cp.linspace(-0.1, 0.25, wavelength_point_num)

# Cruciformscan in alpha direction         -30' ~ 30'
angle_point_num_alpha = 61
offaxis_angle_x_alpha = cp.linspace(-cp.pi /
                                    360, cp.pi/360, angle_point_num_alpha)
offaxis_angle_y_alpha = cp.zeros(angle_point_num_alpha)

# Cruciformscan in beta direction          -30' ~ 30'
angle_point_num_beta = 61
offaxis_angle_x_beta = cp.zeros(angle_point_num_beta)
offaxis_angle_y_beta = cp.linspace(-cp.pi /
                                   360, cp.pi/360, angle_point_num_beta)

# read pixel to world matrix: Tx and Ty
coeff = np.load('data_utils//pixel_to_world//coeff_4096.npz')

Tx_4096=coeff['Tx']
Ty_4096=coeff['Ty']

# %%


def calculate_DN_alpha(i):
    '''
    DN in wavelength list in angle_point_num_alpha. For parallel processing

    Returns
    -------
    ndarray
        DN_alpha 

    '''
    return calculating_DN_4096(wavelength_list,
                          offaxis_angle_x_alpha[i], offaxis_angle_y_alpha[i])


def calculate_DN_beta(j):
    '''
    DN in wavelength list in angle_point_num_beta. For parallel processing

    Returns
    -------
    ndarray
        DN_beta 

    '''
    return calculating_DN_4096(wavelength_list,
                          offaxis_angle_x_beta[j], offaxis_angle_y_beta[j])


# %% 4096




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


    #     x                         shape: (25,)
    #     amplitude, mean, stddev   shape:(2048,2048)
    # Use a list comprehension to calculate the Gaussian curve for each wavelength

    results = np.array([amplitude * np.exp(-(x - mean) ** 2 / (2 * stddev ** 2))
                        for x in wavelength_list])
    return results



def calculating_DN_4096_np(image,wavelength_list, offaxis_angle_x, offaxis_angle_y,dtype=np.float64):
    '''
    Add up each the DN of each pixel 

    Parameters
    ----------
    image : numpy.ndarray shape:(4096,4096)

    wavelength : a number near 30.38 (nm)

    offaxis_angle_x : offaxis alpha angle of center of the image/Sun

    offaxis_angle_y : offaxis beta angle of center of the image/Sun

    Returns
    -------
    DN(digital number): at a given offaxis angle and a give wavelength

    '''

    [image_shape_x, image_shape_y]=image.shape
    image=np.array(image,dtype=dtype)
    # ensure that the image is 4096*4096, if not raise error
    if image_shape_x != 4096 or image_shape_y != 4096:
        raise ValueError("The shape of image is not 4096*4096")
 
    

    # This assupmtion is actually nonsense, and will be solved in Chpater 4
    stddev = np.full((image_shape_x, image_shape_y),0.1 *gaussian_fwhm_to_sigma ) # unit: nm

    # Create NumPy arrays for pixel indices and image data
    Tx = Tx_4096+offaxis_angle_x  # P42 步骤三 四 将卫星整体偏转
    Ty = Ty_4096+offaxis_angle_y  # P42 步骤三 四 将卫星整体偏转

    
    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image / (np.sqrt(2 * np.pi) * stddev)
    mean = wavelength_shift(Tx, Ty)
    coeff = np.array([amplitude, mean, stddev])
    # Compute total_irradiance using vectorized NumPy operations
    total_irradiance = np.sum(my_Gaussian1D(
        wavelength_list, *coeff), axis=(1, 2))  # P42 步骤二

    return total_irradiance











