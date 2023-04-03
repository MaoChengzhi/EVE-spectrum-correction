import numpy as np
from scipy.optimize import fsolve
import pandas as pd
import math
from math import sqrt
from math import pi
from math import e
from scipy.optimize import root

import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
# %%
test_A = [1, 2]
test_central = [3, 2]
test_stddev = [1, 2]

df_test = pd.DataFrame(
    {'amplitude': test_A, 'central_wavelength': test_central, 'stddev': test_stddev, })

# %%


def equations(p, test_A, test_central, test_stddev, j):
    A, mu, sigma = p

    eq1 = A/(2*sqrt(pi)*sigma)
    eq2 = 0
    eq3 = A*sigma/(4*sqrt(pi))
    # print(df)
    # for i in range(pixel_num):
    for i in range(2):

        A_i = test_A[i]
        mu_i = test_central[i]
        sigma_i = test_stddev[i]

        eq1 = eq1-A_i * e**(-(mu_i-mu)**2/(2*(sigma_i**2+sigma**2)))    \
            / (sqrt(2*pi*(sigma_i**2+sigma**2)))

        eq2 = eq2-A_i * (mu_i-mu)*(sigma**2) * e**(-(mu-mu_i)**2/(2*(sigma**2+sigma_i**2))) \
            / (sqrt(2*pi)*(sigma_i**2+sigma**2)**(3/2))

        eq3 = eq3-A_i * (sigma**2) * ((mu_i-mu)**2 * (sigma**2) + (sigma**2)*(sigma_i**2) + sigma_i**4) * \
            e**(-(mu_i-mu)**2/(2*(sigma_i**2+sigma**2))) / \
            (sqrt(2*pi)*(sigma**2+sigma_i**2)**(2.5))

        # print("eq1")
    # print(eq1)
    # print(eq2)
    # print(eq3)
        # print(df)
    # print(A, mu ,sigma)
    return [eq1, eq2, eq3]


# %%
# pixel_num=df.index.stop
i = 1
A, mu, sigma = fsolve(equations, x0=(2.83541144, 3.3481455, 2.80349515,), xtol=1e-10, maxfev=50,
                      args=(test_A, test_central, test_stddev, i))
print("result")
print(A, mu, sigma)

# %%
num = 2
c = []
wave_list = np.linspace(-7, 8, 200)
for i in range(num):
    c.append(models.Gaussian1D(
        amplitude=test_A[i], mean=test_central[i], stddev=test_stddev[i]))

total = np.zeros_like(c[0](wave_list))

for i in range(num):
    total += c[i](wave_list)

c_init = models.Gaussian1D(amplitude=5, mean=1, stddev=1)
fit_c = fitting.LevMarLSQFitter()
c_fitted = fit_c(c_init, wave_list, total)
c_fitted


fig, ax = plt.subplots()

for i in range(num):
    ax.plot(wave_list, c[i](wave_list), label=str(i))

ax.plot(wave_list, total, label="sum up")
ax.plot(wave_list, c_fitted(wave_list), label="fit")
ax.plot(wave_list, models.Gaussian1D(amplitude=A,
        mean=mu, stddev=sigma)(wave_list), label="mine")

ax.legend()
c_fitted
# %%

# fig, ax = plt.subplots()
dim_A = 50
dim_M = 60
A = np.linspace(2.5, 3.2, dim_A)
M = np.linspace(2.2, 2.6, dim_M)
error = np.zeros((dim_A, dim_M))
point = np.zeros((dim_A, dim_M, 2))
for i in range(len(A)):
    for j in range(len(M)):
        error[i, j] = sum((models.Gaussian1D(amplitude=A[i], mean=M[j],
                                             stddev=1.61610393)(wave_list)-total)**2)
        # 1.61610393       1.8034931
        point[i, j] = [A[i], M[j]]

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.scatter3D(point[:, :, 0], point[:, :, 1], error, zdir='z')
ax.set_xlabel('A')
ax.set_ylabel('central_wave')
