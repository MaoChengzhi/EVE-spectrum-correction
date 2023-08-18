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
coeff_file = os.path.join(coeff_file_path, 'coeff.npz')

# Load data from the 'coeff.npz' file
coeff = np.load(coeff_file)

Tx_4096=cp.array(coeff['Tx_4096'])
Ty_4096=cp.array(coeff['Ty_4096'])
Tx_2048=cp.array(coeff['Tx_2048'])
Ty_2048=cp.array(coeff['Ty_2048'])
Tx_1024=cp.array(coeff['Tx_1024'])
Ty_1024=cp.array(coeff['Ty_1024'])
Tx_512=cp.array(coeff['Tx_512'])
Ty_512=cp.array(coeff['Ty_512'])
Tx_256=cp.array(coeff['Tx_256'])
Ty_256=cp.array(coeff['Ty_256'])

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

#define a function to select Tx, Ty according to the shape of image
def select_Tx_Ty(image_shape_x, image_shape_y):
    '''
    Parameters
    ----------
    image_shape_x : TYPE
        DESCRIPTION.
    image_shape_y : TYPE
        DESCRIPTION.

    Returns
    -------
    None.    

    '''

    # choose Tx, Ty according to the shape of image
    if [image_shape_x, image_shape_y]==[4096,4096]:
        Tx0=Tx_4096
        Ty0=Ty_4096
    elif [image_shape_x, image_shape_y]==[2048,2048]:
        Tx0=Tx_2048
        Ty0=Ty_2048
    elif [image_shape_x, image_shape_y]==[1024,1024]:
        Tx0=Tx_1024
        Ty0=Ty_1024
    elif [image_shape_x, image_shape_y]==[512,512]:
        Tx0=Tx_512
        Ty0=Ty_512
    elif [image_shape_x, image_shape_y]==[256,256]:
        Tx0=Tx_256
        Ty0=Ty_256
    else:
        raise ValueError('The shape of image is not 4096*4096, 2048*2048 or 1024*1024')
    
    return Tx0,Ty0

    

def my_Gaussian1D(wavelength_list, amplitude, mean, stddev):

    # Expand the dimensions of wavelength_list to match the shape of amplitude, mean, and stddev
    expanded_wavelengths = cp.expand_dims(wavelength_list, axis=(1, 2))

    # Calculate the Gaussian curve for all wavelengths simultaneously using Cupy element-wise operations
    results = amplitude * cp.exp(-((expanded_wavelengths - mean) ** 2) / (2 * stddev ** 2))

    return results


def calculating_DN(image,wavelength_list, offaxis_angle_x, offaxis_angle_y,dtype=cp.float64):
    '''
    Add up each the DN of each pixel 

    Parameters   
    ----------.plkj; 
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
    Tx0,Ty0=select_Tx_Ty(image_shape_x, image_shape_y)

    

    # turn numpy array into cupy array
    wavelength_list=cp.asarray(wavelength_list)

    #                   !!----------------50ms-------------------------!!
    if isinstance(image, np.ndarray):
        image=cp.asarray(image,dtype=dtype)   
    

    # This assupmtion is actually nonsense, and will be solved in Chpater 4
    stddev = cp.full((image_shape_x, image_shape_y),0.1 *gaussian_fwhm_to_sigma ) # unit: nm

    # Create NumPy arrays for pixel indices and image data
    Tx = Tx0+offaxis_angle_x  # P42 步骤三 四 将卫星整体偏转
    Ty = Ty0+offaxis_angle_y  # P42 步骤三 四 将卫星整体偏转

    
    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image / (cp.sqrt(2 * cp.pi) * stddev)
    mean = wavelength_shift(Tx, Ty)
    coeff = cp.array([amplitude, mean, stddev])
    # Compute total_irradiance using vectorized NumPy operations
    
    
    #    my_Gaussian1D(wavelength_list, *coeff)        
    total_irradiance = cp.sum(my_Gaussian1D(
        wavelength_list, *coeff), axis=(1, 2))  # P42 步骤二

    return total_irradiance.get()  # turn cupy array into numpy array







