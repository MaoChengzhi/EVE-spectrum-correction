import numpy as np
import cupy as cp
import os 

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




# Get the path of the current Python file
current_py_file = os.path.abspath(__file__)
# Construct the path of the 'coeff_4096.npz' file relative to the Python file
coeff_file_path = os.path.join(os.path.dirname(current_py_file), 'pixel_to_world')
coeff_file = os.path.join(coeff_file_path, 'coeff_4096.npz')

# Load data from the 'coeff_4096.npz' file
coeff = np.load(coeff_file)

Tx_4096=cp.array(coeff['Tx'])
Ty_4096=cp.array(coeff['Ty'])



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


# def my_Gaussian1D(wavelength_list, amplitude, mean, stddev):
#     '''
#     I use this function written myself, because Gaussian1D in astropy is too slow.
#     Returns
#     -------
#     Value of the 1D Gaussian curve at a given point	
#     '''


#     #     wavelength_list  cupy array   shape: (25,)
    
#     #     amplitude   cupy array        shape:(2048,2048)
#     #     mean        cupy array        shape:(2048,2048)
#     #     stddev      cupy array        shape:(2048,2048)
    
#     # Use a list comprehension to calculate the Gaussian curve for each wavelength

#     results = cp.array([amplitude * cp.exp(-(x - mean) ** 2 / (2 * stddev ** 2))
#                         for x in wavelength_list])

#     return results

def my_Gaussian1D(wavelength_list, amplitude, mean, stddev):
    # Check if the input arrays have the same shape
    # assert amplitude.shape == mean.shape == stddev.shape == (4096, 4096), "Input arrays must have shape (2048, 2048)"

    # Expand the dimensions of wavelength_list to match the shape of amplitude, mean, and stddev
    expanded_wavelengths = cp.expand_dims(wavelength_list, axis=(1, 2))

    # Calculate the Gaussian curve for all wavelengths simultaneously using Cupy element-wise operations
    results = amplitude * cp.exp(-((expanded_wavelengths - mean) ** 2) / (2 * stddev ** 2))

    return results


def calculating_DN_4096(image,wavelength_list, offaxis_angle_x, offaxis_angle_y,dtype=cp.float64):
    '''
    Add up each the DN of each pixel 

    Parameters   
    ----------
    image : numpy.ndarray shape:(4096,4096)
                or cupy array shape:(4096,4096)
                
    wavelength : a number near 30.38 (nm)

    offaxis_angle_x : offaxis alpha angle of center of the image/Sun

    offaxis_angle_y : offaxis beta angle of center of the image/Sun

    Returns
    -------
    DN(digital number): at a given offaxis angle and a give wavelength

    '''

    [image_shape_x, image_shape_y]=image.shape
    # ensure that the image is 4096*4096, if not raise error
    if image_shape_x != 4096 or image_shape_y != 4096:
        raise ValueError("The shape of image is not 4096*4096")
    # turn array into cupy array
    wavelength_list=cp.asarray(wavelength_list)

    #                   !!----------------50ms-------------------------!!
    if isinstance(image, np.ndarray):
        image=cp.asarray(image,dtype=dtype)   
    

    # This assupmtion is actually nonsense, and will be solved in Chpater 4
    stddev = cp.full((image_shape_x, image_shape_y),0.1 *gaussian_fwhm_to_sigma ) # unit: nm

    # Create NumPy arrays for pixel indices and image data
    Tx = Tx_4096+offaxis_angle_x  # P42 步骤三 四 将卫星整体偏转
    Ty = Ty_4096+offaxis_angle_y  # P42 步骤三 四 将卫星整体偏转

    
    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image / (cp.sqrt(2 * cp.pi) * stddev)
    mean = wavelength_shift(Tx, Ty)
    coeff = cp.array([amplitude, mean, stddev])
    # Compute total_irradiance using vectorized NumPy operations
    
    
    #    my_Gaussian1D(wavelength_list, *coeff)         !!-------------350ms----------------!!
    total_irradiance = cp.sum(my_Gaussian1D(
        wavelength_list, *coeff), axis=(1, 2))  # P42 步骤二

    return total_irradiance.get()  # turn cupy array into numpy array







