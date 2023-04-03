# This file aims to draw conclusion from DN.npz
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math
from calculating_DN_2048 import wavelength_point_num, wavelength_list, angle_point_num_alpha
from calculating_DN_2048 import offaxis_angle_x_alpha, offaxis_angle_y_alpha

DN = np.load("output_DN/DN_large_lambda_range_2048.npz")

DN_alpha = np.zeros((angle_point_num_alpha, wavelength_point_num))
# %%
# Offaxis angle during cruciformscan
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(range(angle_point_num_alpha), offaxis_angle_x_alpha)
ax.plot(range(angle_point_num_alpha), offaxis_angle_y_alpha)
# %%
# Profiles during cruciformscan
fig, ax = plt.subplots()
# Profiles during cruciformscan in alpha direction
for i in range(angle_point_num_alpha):
    ax.plot(wavelength_list, DN['DN_alpha'][i], label='linear')
# ax.set_title("He II 谱线轮廓随入射偏角𝜶变化的模拟结果")
ax.set_title("Full-disk irradiance profiles at alpha offset angles")

# %%
# Fit data in DN_alpha.npz
wavelength_shift_alpha = np.zeros(angle_point_num_alpha)
fit_alpha = []   # List of Gaussian1D
for i in range(angle_point_num_alpha):
    g_init = models.Gaussian1D(amplitude=3E9, mean=0.05, stddev=0.0424)
    # initial value for fitting
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, wavelength_list, DN['DN_alpha'][i])
    wavelength_shift_alpha[i] = g.mean.value
    fit_alpha.append(g)

# %%
# Panned central wavelength shift
# Y 轴的零点被设定为全日面 He II 谱线在没有任何 SDO 卫星偏转时的中心波长位置，
# 也就是𝛼 = 0且𝛽 = 0的情况

fig, ax = plt.subplots()
ax.plot(offaxis_angle_x_alpha, wavelength_shift_alpha)
ax.set_ylabel('Wavelength shift (nm)')
ax.set_xlabel("Alpha Offset (rad)")
