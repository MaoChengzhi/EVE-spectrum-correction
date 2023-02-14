import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

# Generate fake data
rng = np.random.default_rng(0)
x = np.linspace(-5., 5., 200)
y = 3 * np.exp(-0.5 * (x - 1.3)**2 / 0.8**2)
y += rng.normal(0., 0.2, x.shape)


# Fit the data using a Gaussian
g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, x, y)
# %%
# Plot the data with the best-fit model
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'ko')

plt.plot(x, g(x), label='Gaussian')
plt.xlabel('Position')
plt.ylabel('Flux')
plt.legend(loc=2)

# %%
# Vectorize the calculation of DN values
DN_alpha = calculating_DN(
    wavelength_list, offaxis_angle_x_alpha[:, np.newaxis], offaxis_angle_y_alpha[:, np.newaxis])
DN_beta = calculating_DN(
    wavelength_list, offaxis_angle_x_beta[:, np.newaxis], offaxis_angle_y_beta[:, np.newaxis])
