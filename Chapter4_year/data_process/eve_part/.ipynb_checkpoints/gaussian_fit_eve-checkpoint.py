import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math

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

    Examples
    --------
    >>> import numpy as np
    >>> x = np.linspace(-1, 1, 101)
    >>> y = np.exp(-0.5*(x/0.1)**2)
    >>> mean = gaussian_fit(y)
    >>> print(mean)
    0.0
    '''
    
    # if(np.sum(np.isnan(irradiance))>0):
    #     print('nan error')
    # if((irradiance <= 0).any()):
    #     print('minus')
    # if(np.max(irradiance)<1e-4):
    #     print('peak')
        
    if(np.sum(np.isnan(irradiance))>0 
       or (irradiance <= 0).any()  
       or np.max(irradiance)<1e-4
      ):
        print("error 1")
        return np.nan,np.nan,np.nan
    
    
    
    g_init = models.Gaussian1D(amplitude=0.005, mean=30.3, stddev=0.0424)

    # initial value for fitting
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, wavelength_list, irradiance)
    if(g.stddev>0.1):
        print("unsuccessful fitting")
        return np.nan,np.nan,np.nan
    mean = g.mean.value
    stddev=g.stddev.value
    amplitude=g.amplitude.value
    return amplitude,mean,stddev
