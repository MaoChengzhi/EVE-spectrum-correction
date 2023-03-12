import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math

# DN = np.load("DN_above0_fulldisk.npz")
# DN_alpha = DN['DN_alpha']


def iteration(DN_alpha):
    # %%
    # Initialize
    wavelength_point_num = 15
    wavelength_list = np.linspace(-0.1, 0.15, wavelength_point_num)

    # Cruciformscan in alpha direction
    angle_point_num_alpha = 61
    # DN_alpha = np.zeros((angle_point_num_alpha, wavelength_point_num))
    offaxis_angle_x_alpha = np.linspace(-math.pi /
                                        360, math.pi/360, angle_point_num_alpha)

    # %%
    wavelength_shift_alpha = np.zeros(angle_point_num_alpha)
    fit_alpha = []   # List of Gaussian1D
    for i in range(angle_point_num_alpha):
        g_init = models.Gaussian1D(amplitude=3E9, mean=0.05, stddev=0.0424)
        # initial value for fitting
        fit_g = fitting.LevMarLSQFitter()
        g = fit_g(g_init, wavelength_list, DN_alpha[i])
        wavelength_shift_alpha[i] = g.mean.value
        fit_alpha.append(g)

    # %%
    fig, ax = plt.subplots()
    ax.plot(offaxis_angle_x_alpha, wavelength_shift_alpha -
            wavelength_shift_alpha[int(angle_point_num_alpha/2)])
    ax.set_ylabel('Wavelength shift (nm)')
    ax.set_xlabel("Alpha Offset (rad)")

    # %%
    a_init = models.Polynomial1D(degree=2)
    fit_a = fitting.LevMarLSQFitter()
    a = fit_a(a_init, offaxis_angle_x_alpha, wavelength_shift_alpha -
              wavelength_shift_alpha[int(angle_point_num_alpha/2)])
    return a.c2.value
