import astropy.units as u
from sunpy.net import Fido, attrs as a
import glob
import sunpy.map
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
# %%
aia_files = sorted(glob.glob('data/AIA/*image_lev1.fits'))
m_aia = sunpy.map.Map(aia_files)

# %%
test = m_aia[0]
b = test.center
a = test.pixel_to_world(2048*u.pixel, 2048*u.pixel)
# %%
# Tx_list,Ty_list
Tx_list = []
Ty_list = []
for aia_map in m_aia:
    Tx_list.append(aia_map.center.Tx.value)
    Ty_list.append(aia_map.center.Ty.value)

# regular expression
strings = aia_files

time_pattern = r'\d{2}_\d{2}_\d{2}_\d{2}'
time = []  # hh_mm_ss_ms     ms: 231 ms -> 23
for string in strings:
    match = re.search(time_pattern, string)
    if match:
        # print(match.group(0))
        time.append(match.group(0))
# %%
data = {
    "alpha_list": Tx_list,
    "beta_list": Ty_list,
    "time": time
}
frame = pd.DataFrame(data)

# %%   #plot

num = 100
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots(2, 1)  # Create a figure and an axes.

# ax.scatter(Tx_list[:num], Ty_list[:num], label='fuck',  cmap=plt.cm.Blues,
#  edgecolors='none',)  # Plot some data on the axes.

ax[0].plot(Tx_list[:num], Ty_list[:num])

ax[0].set_xlabel('alpha /arcsec')
ax[0].set_yticks([-100, 100])
ax[0].set_ylabel('beta /arcsec')  # Add a y-label to the axes.
# ax.set_title("Simple Plot")  # Add a title to the axes.
ax[0].set_title('first {} iamges'.format(num))
ax[0].legend()  # Add a legend.

ax[1].plot(Tx_list, Ty_list,)
ax[1].set_xlabel('alpha /arcsec')  # Add an x-label to the axes.
ax[1].set_yticks([-100, 100])
ax[1].set_ylabel('beta /arcsec')  # Add a y-label to the axes.
ax[1].set_title('all iamges')  # Add a title to the axes.


# %%
fig, ax = plt.subplots()
sc = ax.scatter(Tx_list, Ty_list, s=100, c=range(len(Tx_list)), alpha=0.5,)
ax.legend()
fig.colorbar(sc)
# %%
frame.plot()
# %%
min_index = np.argmin(Ty_list)
frame.loc[min_index]
