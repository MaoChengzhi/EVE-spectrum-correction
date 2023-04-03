# This file aims to draw conclusion from DN.npz
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math
from astropy.constants import au, R_sun
from calculating_DN_2048 import wavelength_point_num, wavelength_list, angle_point_num_alpha
from calculating_DN_2048 import offaxis_angle_x_alpha, offaxis_angle_y_alpha

transunit = ((au/R_sun).value)**2 / 1000
DN = np.load("output_DN/DN_small_range_2048.npz")
DN_alpha_list = DN["DN_alpha_list"]  # DN_alpha_list.shape= (10, 61, 15)
a_list = DN['a_list']
a_num = len(a_list)


offaxis_angle_x_min_alpha = offaxis_angle_x_alpha*180*60/math.pi


# =============================================================================
# # Cruciformscan in beta direction
# angle_point_num_beta = 61
# DN_beta = np.zeros((angle_point_num_beta, wavelength_point_num))
# offaxis_angle_x_beta = np.zeros(angle_point_num_beta)
# offaxis_angle_y_beta = np.linspace(-math.pi /
#                                    360, math.pi/360, angle_point_num_beta)
# offaxis_angle_y_min_beta = offaxis_angle_y_beta*180*60/math.pi
# =============================================================================
# %%
# Profiles during cruciformscan
fig, ax = plt.subplots()
# Profiles during cruciformscan in alpha direction
for i in range(angle_point_num_alpha):
    ax.plot(wavelength_list, DN_alpha_list[0][i], label='linear')
# ax.set_title("He II 谱线轮廓随入射偏角𝜶变化的模拟结果")
ax.set_title("Full-disk irradiance profiles at alpha offset angles")

# %%
wavelength_shift_alpha = np.zeros((a_num, angle_point_num_alpha))
fit_alpha = []   # List of Gaussian1D
for i in range(a_num):
    for j in range(angle_point_num_alpha):
        g_init = models.Gaussian1D(amplitude=1E9, mean=0.05, stddev=0.0424)
        # initial value for fitting
        fit_g = fitting.LevMarLSQFitter()
        g = fit_g(g_init, wavelength_list, DN_alpha_list[i][j])
        wavelength_shift_alpha[i][j] = g.mean.value
        fit_alpha.append(g)
# %%
fig, ax = plt.subplots()
for i in range(a_num):
    # ax.plot(offaxis_angle_x_alpha,
    #         wavelength_shift_alpha[i]\
    #             -wavelength_shift_alpha[i][int(angle_point_num_alpha/2)])
    ax.plot(offaxis_angle_x_min_alpha, wavelength_shift_alpha[i],
            label="{:.2f}".format(a_list[i]/transunit))
    ax.set_xlim(-30, 30)

ax.plot(offaxis_angle_x_min_alpha, 19.8*transunit*offaxis_angle_x_alpha**2,
        label="Chamberlin obs")
ax.legend()
# %% Fit the output A

# Define the polynomial model
model = models.Polynomial1D(degree=2)

# Define the fitter
fitter = fitting.LevMarLSQFitter()

fitted_model = []
for i in range(a_num):
    # Fit the model to the data
    fitted_model.append(
        fitter(model, offaxis_angle_x_alpha, wavelength_shift_alpha[i]))
# %%
c1_list = []
for i in range(a_num):
    c1_list.append(fitted_model[i].c1.value)
fig, ax = plt.subplots()
ax.plot(a_list/transunit, c1_list/transunit)
# %%
c2_list = []
for i in range(a_num):
    c2_list.append(fitted_model[i].c2.value)
fig, ax = plt.subplots()
ax.plot(a_list/transunit, c2_list/transunit)
ax.scatter(a_list/transunit, c2_list/transunit)
