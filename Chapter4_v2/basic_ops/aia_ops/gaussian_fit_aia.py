import numpy as np
import cupy as cp
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math

# %%
def gaussian_fit_aia(wavelength_list, irradiance):
    '''
    Fit a Gaussian function to the given irradiance data.

    Parameters
    ----------
    irradiance : ndarray
        A 1D array of irradiance data to fit the Gaussian function to.

    Returns
    -------
    float
        The mean value of the fitted Gaussian function.

    Notes
    -----
    The function uses the astropy modeling and fitting library to perform the fitting. It sets the initial parameters of the Gaussian function to amplitude=1E9, mean=0.05, and stddev=0.0424, and uses the LevMarLSQFitter algorithm for fitting.


    '''
    
    if(np.sum(np.isnan(irradiance))!=0):
        return np.nan,np.nan,np.nan

    try:
        g_init = models.Gaussian1D(amplitude=1E9, mean=30.3783, stddev=0.03)
        #
        # initial value for fitting
        fit_g = fitting.LevMarLSQFitter()
        g = fit_g(g_init, wavelength_list, irradiance)
        amplitude=g.amplitude.value
        mean = g.mean.value
        stddev=g.stddev.value
        return amplitude,mean,stddev
    except:
        return np.nan,np.nan,np.nan
