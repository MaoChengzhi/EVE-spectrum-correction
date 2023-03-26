import numpy as np
from scipy.optimize import fsolve
import pandas as pd
import math
from math import sqrt
from math import pi
from math import e
from scipy.optimize import root
import time
from multiprocessing import Pool

import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

from image_df_2048 import image_df_2048

from astropy.constants import au, R_sun
# %%
transunit = ((au/R_sun).value)**2 / 1000
angle_point_num_alpha = 61
offaxis_angle_x_alpha = np.linspace(-math.pi /
                                    360, math.pi/360, angle_point_num_alpha)
offaxis_angle_y_alpha = np.zeros(angle_point_num_alpha)
# %%


def equations(p, A_i, mu_i, sigma_i):
    mu, sigma = p
    eq1 = 0
    eq2 = 0
    exp_i = np.exp(-(mu - mu_i) ** 2 / (2 * (sigma ** 2 + sigma_i ** 2)))
    eq1 = np.sum(A_i * exp_i * (1 / np.sqrt(sigma ** 2 + sigma_i ** 2) - 2 * (sigma ** 2 * (mu - mu_i)
                 ** 2 + sigma ** 2 * sigma_i ** 2 + sigma_i ** 4) / (sigma ** 2 + sigma_i ** 2) ** 2.5))
    eq2 = np.sum(A_i * (mu_i - mu) * exp_i /
                 ((sigma_i ** 2 + sigma ** 2) ** (3 / 2)))
    # print(eq1,eq2,mu ,sigma)
    return [eq1, eq2]
# %%


def fit(i):
    df = image_df_2048(i)
    A_i = df.iloc[:]["integral_area"]
    mu_i = df.iloc[:]["central_wavelength"]
    sigma_i = df.iloc[:]["stddev"]
    sol = fsolve(equations, x0=(19.8*transunit*offaxis_angle_x_alpha[i]**2+0.004, 0.042),
                 args=(A_i, mu_i, sigma_i,), maxfev=20)
    print(str(offaxis_angle_x_alpha[i]*180*60/math.pi)+" arcmin:   finished")
    print(sol)
    print()
    return sol


# %%
start = time.time()
if __name__ == '__main__':
    with Pool(processes=12) as p:  # CPU on my laptop with 14 cores
        solution = np.array(
            p.map(fit, range(angle_point_num_alpha)))


end = time.time()
totol_time = end - start
print(totol_time)
