import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# %%


def gaussian_fit_eve(wavelength_list, irradiance):
    '''
    Fit a Gaussian function to the given irradiance data.

    Parameters
    ----------
    irradiance : (12,) ndarray
        A 1D array of irradiance data to fit the Gaussian function to.

    Returns
    -------
    float
        The mean value of the fitted Gaussian function.

    Notes
    -----
    The function uses the astropy modeling and fitting library to perform the fitting. It sets the initial parameters of the Gaussian function to amplitude=1E9, mean=0.05, and stddev=0.0424, and uses the LevMarLSQFitter algorithm for fitting.

    The function also imports a pre-defined list of wavelengths from the constant module, which is used to evaluate the fitted Gaussian function.

    '''
    
    # Perform the curve fitting


    #check whether input contain nan
    try:
        if np.any(np.isnan(irradiance)):
            raise ValueError("Input data contains NaN values.")

        p0 = [0.005, 30.3, 0.03]  # Initial guess for the parameters [amplitude, mean, stddev]
        popt, pcov = curve_fit(gaussian_function, wavelength_list, irradiance, p0=p0)

        return popt, pcov

    except :
        return np.full((3, ), np.nan), np.full((3, 3), np.nan)



def gaussian_function(x, amplitude, mean, stddev):
    # A refers to Amplitude, the peak value!   not the integrated area!
    return amplitude * np.exp(-(x - mean)**2 / (2 * stddev**2))
