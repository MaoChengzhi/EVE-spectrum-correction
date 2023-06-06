import datetime
from .pixel_to_world.my_pixel_to_world import my_pixel_to_world
from .data.constant import wavelength_list_aia_relative

from astropy.stats import gaussian_fwhm_to_sigma
import cupy as cp
import pandas as pd
from math import pi

import os 

import astropy.units as u
from astropy.constants import G, M_sun, R_sun, au
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from astropy.units import imperial
# %%


def calculate_DN(aia_adjusted_map, a=0, b=0,c=0, d=0,  e=0):
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
    time=datetime.datetime.strptime(aia_adjusted_map.meta['t_rec'],'%Y-%m-%dT%H:%M:%SZ')
    radial_doppler=(calculate_relative_radial_velocity(time) ).to(u.nm,
                                equivalencies=u.doppler_optical(30.3783 * u.nm)).value-30.3783
    
    
    image_data = cp.array(aia_adjusted_map.data)
    image_shape_x, image_shape_y = image_data.shape

    #read the eve stddev:
    module_dir = os.path.dirname(os.path.abspath(__file__))
    eve_file=os.path.join(module_dir,'data','EVE_daily','daily_data.csv')
    
    try:
        daily_fit_df=pd.read_csv(eve_file)
        daily_fit_df=daily_fit_df.set_index('time')
        daily_fit_df.index = pd.to_datetime(daily_fit_df.index)

        date_obj = time.date()
        time_obj = datetime.time(0, 0)
        date=datetime.datetime.combine(date_obj, time_obj)
        stddev_eve=daily_fit_df.loc[date]['stddev']*0.981
    except:
        stddev_eve=0.03
        print('EVE daily data not found, use default value 0.03')

    # fixed stddev for all
    # stddev_eve=0.03
    # stddev = cp.full((image_shape_x, image_shape_y),stddev_eve )# unit: nm
    
    # Create NumPy arrays for pixel indices and image data
    pixel_x = cp.arange(image_shape_x)
    pixel_y = cp.arange(image_shape_y)
    Px, Py = cp.meshgrid(pixel_x, pixel_y, indexing='ij')

    # Compute Tx and Ty for all pixels in parallel
    Tx, Ty = my_pixel_to_world(Px, Py)  # 使用4096的照片

    # only use pixels with value>0
    image_data = image_data*(image_data > 0)

    stddev =get_stddev(image_data)
    # Compute amplitude, mean, and stddev for all pixels in parallel
    amplitude = image_data / (cp.sqrt(2 * pi) * stddev)
    mean = wavelength_shift(Tx, Ty, a,b,c, d, e)+radial_doppler
    coeff = cp.array([amplitude, mean, stddev])

    # Compute total_irradiance using vectorized NumPy operations
    total_irradiance = cp.sum(my_Gaussian1D(
        wavelength_list_aia_relative, *coeff), axis=(1, 2))  # size:(12,4096,4096)

    return date,total_irradiance.get()

# %%


def wavelength_shift(Tx, Ty, a,b,c ,d, e):
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

    return a * Tx**2 + b * Tx +c*Ty**2+d * Ty+e


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


def calculate_relative_radial_velocity(time):
    # Convert the input time to an Astropy Time object

    t = Time(time)

    # Get the barycentric position and velocity of the Earth
    earth_posvel = get_body_barycentric_posvel('earth', t)
    # Get the barycentric position and velocity of the Sun
    sun_posvel = get_body_barycentric_posvel('sun', t)

    # Calculate the relative position of the Earth with respect to the Sun
    relative_pos = earth_posvel[0] - sun_posvel[0]
    # Calculate the relative velocity of the Earth with respect to the Sun
    relative_vel = earth_posvel[1] - sun_posvel[1]

    # Calculate the radial component of the relative velocity
    radial_velocity = (relative_pos.get_xyz() * relative_vel.get_xyz()).sum() / relative_pos.norm()
    # Convert the velocity to km/s
    radial_velocity = radial_velocity.to(u.km/u.s)

    # print('time correction')
    return radial_velocity

def get_stddev(input_array):
    lower_threshold = 8
    upper_threshold = 150
    lower_value = 0.028
    upper_value = 0.036
    
    output_array = cp.where(input_array < lower_threshold, lower_value, cp.where(input_array > upper_threshold, upper_value, lower_value + (input_array - lower_threshold) * (upper_value - lower_value) / (upper_threshold - lower_threshold)))
    
    return output_array