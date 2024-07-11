import numpy as np
import cupy as cp
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
from scipy.optimize import curve_fit


# %%


# def gaussian_fit_aia(wavelength_list, irradiance):
#     '''
#     Fit a Gaussian function to the given irradiance data.

#     Parameters
#     ----------
#     irradiance : ndarray
#         A 1D array of irradiance data to fit the Gaussian function to.

#     Returns
#     -------
#     float
#         The mean value of the fitted Gaussian function.

#     Notes
#     -----
#     The function uses the astropy modeling and fitting library to perform the fitting. It sets the initial parameters of the Gaussian function to amplitude=1E9, mean=0.05, and stddev=0.0424, and uses the LevMarLSQFitter algorithm for fitting.

#     The function also imports a pre-defined list of wavelengths from the constant module, which is used to evaluate the fitted Gaussian function.

#     Examples
#     --------
#     >>> import numpy as np
#     >>> x = np.linspace(-1, 1, 101)
#     >>> y = np.exp(-0.5*(x/0.1)**2)
#     >>> mean = gaussian_fit(y)
#     >>> print(mean)
#     0.0
#     '''

#     g_init = models.Gaussian1D(amplitude=1E9, mean=0.05, stddev=0.0424)
#     #
#     # initial value for fitting
#     fit_g = fitting.LevMarLSQFitter()
#     g = fit_g(g_init, wavelength_list, irradiance)
#     mean = g.mean.value

#     return mean



def gaussian_fit_aia(wavelength_list, irradiance, initial_guess):
    '''
    Fit a Gaussian function to the given irradiance data.

    Parameters
    ----------
    wavelength_list :  ndarray
        An 1D array of wavelengths corresponding to the irradiance data.
    irradiance :  ndarray
        An 1D array of irradiance data to fit the Gaussian function to.
    initial_guess :  (3,) ndarray
        An 1D array of initial guesses for the parameters [amplitude, mean, stddev] of the Gaussian function.


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

        p0 = initial_guess  # Initial guess for the parameters [amplitude, mean, stddev]
        popt, pcov = curve_fit(gaussian_function, wavelength_list, irradiance, p0=p0)

        return popt, pcov

    except :
        return np.full((3, ), np.nan), np.full((3, 3), np.nan)



def gaussian_function(x, amplitude, mean, stddev):
    # A refers to Amplitude, the peak value!   not the integrated area!
    return amplitude * np.exp(-(x - mean)**2 / (2 * stddev**2))